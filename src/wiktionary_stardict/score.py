# https://www.mediawiki.org/wiki/Extension:Score
# https://lilypond.org/doc/v2.26/Documentation/usage/other-programs
from pathlib import Path

LILYPOND_VERSION = ""


def get_lilypond_version() -> str:
    from subprocess import run

    p = run(["lilypond", "-v"], check=True, text=True, capture_output=True)
    return p.stdout[: p.stdout.find("(")].removeprefix("GNU LilyPond").strip()


def create_lilypond_code(data: dict) -> str:
    global LILYPOND_VERSION

    if data.get("lang", "lilypond") == "lilypond" and data.get("raw", "0") == "1":
        return data.get("body", {}).get("extsrc", "")

    if LILYPOND_VERSION == "":
        LILYPOND_VERSION = get_lilypond_version()
    code = f"""
\\version "{LILYPOND_VERSION}"
\\paper{{
  indent=0\\mm
  oddFooterMarkup=##f
  oddHeaderMarkup=##f
  bookTitleMarkup=##f
  scoreTitleMarkup=##f
"""
    line_width = data.get("attrs", {}).get("line_width_inches", "")
    if line_width != "":
        code += f"\nline-width={line_width}\\in"
    code += f"""
}}
\\score {{
  {data.get("body", {}).get("extsrc", "")}
}}"""
    return code


def create_bwrap_command(score_path: Path, seccomp_fd: int) -> list[str]:
    command = [
        "bwrap",
        "--unshare-all",
        "--die-with-parent",
        "--new-session",
        "--clearenv",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
    ]
    for ro_bind in [
        "/usr/bin",
        "/usr/lib",
        "/usr/share",
        "/lib",
        "/lib64",
        "/etc",
    ]:
        command.extend(["--ro-bind", ro_bind, ro_bind])
    for create_dir in ["/tmp", "/var"]:
        command.extend(["--dir", create_dir])
    command.extend(
        [
            "--chdir",
            score_path.parent,
            "--setenv",
            "HOME",
            score_path.parent,
            "--bind",
            score_path.parent,
            score_path.parent,
        ]
    )
    path_env = "/usr/bin"
    for lilypond_dir in Path(".").glob("lilypond-*"):
        if lilypond_dir.is_dir():
            sandbox_lilypond_path = score_path.parent / "lilypond"
            command.extend(["--ro-bind", lilypond_dir, sandbox_lilypond_path])
            path_env = str(sandbox_lilypond_path / "bin") + ":/usr/bin"
            break
    command.extend(["--setenv", "PATH", path_env])
    command.extend(
        [
            "--seccomp",
            str(seccomp_fd),
            "--",
            "lilypond",
            "--svg",
            "-dno-use-paper-size-for-page",
            "-dbackend=cairo",
            "-o",
            score_path.with_suffix(""),
            score_path,
        ]
    )
    return command


def add_seccomp_filters(f):
    import errno
    from platform import machine

    import seccomp

    block_list = seccomp.SyscallFilter(seccomp.ALLOW)
    if machine() == "x86_64":
        block_list.add_arch(seccomp.Arch.X86)
    # Copied from https://github.com/igo95862/bubblejail/blob/master/src/bubblejail/services.py
    for syscall in [
        "bdflush",
        "io_pgetevents",
        "kexec_file_load",
        "kexec_load",
        "migrate_pages",
        "move_pages",
        "nfsservctl",
        "nice",
        "oldfstat",
        "oldlstat",
        "oldolduname",
        "oldstat",
        "olduname",
        "pciconfig_iobase",
        "pciconfig_read",
        "pciconfig_write",
        "sgetmask",
        "ssetmask",
        "swapcontext",
        "swapoff",
        "swapon",
        "sysfs",
        "uselib",
        "userfaultfd",
        "ustat",
        "vm86",
        "vm86old",
        "vmsplice",
        "bpf",
        "fanotify_init",
        "lookup_dcookie",
        "perf_event_open",
        "quotactl",
        "setdomainname",
        "sethostname",
        "delete_module",
        "init_module",
        "finit_module",
        "query_module",
        "acct",
        "iopl",
        "ioperm",
        "settimeofday",
        "stime",
        "clock_settime",
        "clock_settime64",
        "vhangup",
    ]:
        block_list.add_rule(seccomp.ERRNO(errno.ENOSYS), syscall)
    block_list.export_bpf(f)


def get_score_svg(title: str, data: dict) -> str:
    from os import environ
    from subprocess import run
    from tempfile import TemporaryDirectory, TemporaryFile

    from .main import logger

    global LILYPOND_VERSION

    if data.get("attrs", {}).get("lang", "") == "ABC":
        # abc2ly document says it's not currently supported
        return ""

    if LILYPOND_VERSION == "":
        LILYPOND_VERSION = get_lilypond_version()

    with TemporaryDirectory(prefix="lilypond_") as dir:
        dir_path = Path(dir)
        score_path = dir_path / "score.ly"
        with open(score_path, "w") as f:
            f.write(create_lilypond_code(data))
        svg_path = score_path.with_suffix(".svg")
        with TemporaryFile() as seccomp_f:
            add_seccomp_filters(seccomp_f)
            seccomp_f.seek(0)
            p = run(
                create_bwrap_command(score_path, seccomp_f.fileno()),
                capture_output=True,
                text=True,
                pass_fds=(seccomp_f.fileno(),),
                env={
                    env_name: environ[env_name]
                    for env_name in ["USER", "USERNAME", "PATH", "HOME"]
                    if environ.get(env_name, "") != ""
                },
            )
            if p.returncode == 0 and svg_path.is_file():
                with open(svg_path) as svg_f:
                    return svg_f.read()
            else:
                logger.error(f'lilypond failed in page "{title}": ' + p.stdout + p.stderr)
                return ""
