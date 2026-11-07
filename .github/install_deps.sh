#!/usr/bin/env bash
set -eux
set -o pipefail

export CFLAGS="-march=native -O3"
sudo apt update
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install
uv sync --extra dev

# compile libseccomp
# copied from https://gitlab.archlinux.org/archlinux/packaging/packages/libseccomp/-/blob/main/PKGBUILD
sudo apt install gperf
libseccomp_ver="2.6.1"
wget -nv https://github.com/seccomp/libseccomp/releases/download/v${libseccomp_ver}/libseccomp-${libseccomp_ver}.tar.gz
tar -xf libseccomp-*.tar.gz
rm libseccomp-*.tar.gz
root_dir=$(pwd)
cd libseccomp-*
uv pip install Cython setuptools build wheel
./configure --prefix=/usr
make -j "$(nproc)"
libseccomp_dir=$(pwd)
cd src/python
VERSION_RELEASE=$libseccomp_ver CPPFLAGS="-I${libseccomp_dir}/include" uv run python -m build --wheel --no-isolation
uv pip install dist/*.whl
cd "$root_dir"
rm -rf libseccomp*

# compile bubblewrap
sudo apt install ninja-build libcap-dev
wget -nv https://github.com/containers/bubblewrap/releases/download/v0.13.1/bubblewrap-0.13.1.tar.xz
tar -xf bubblewrap-*.tar.xz
rm bubblewrap-*.tar.xz
cd bubblewrap-*
uv tool install meson
uv tool update-shell
meson setup build --prefix=/usr --buildtype=release -Dassume_kernel="$(uname -r | grep -oP '^\d+(\.\d+){2}')" -Dselinux=disabled
meson compile -C build -j "$(nproc)"
sudo "$(command -v meson)" install -C build
cd ..
rm -rf bubblewrap*
# https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

# download lilypond
wget -nv https://gitlab.com/lilypond/lilypond/-/releases/v2.26.0/downloads/lilypond-2.26.0-linux-x86_64.tar.gz
tar -xf lilypond-*.tar.gz
rm lilypond-*.tar.gz
echo lilypond-*/bin >> "$GITHUB_PATH"

npm install -g npm@latest
npm install
