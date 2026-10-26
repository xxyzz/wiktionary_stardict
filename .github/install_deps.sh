#!/usr/bin/env bash
set -eux
set -o pipefail

sudo apt update

# compile libseccomp
# copied from https://gitlab.archlinux.org/archlinux/packaging/packages/libseccomp/-/blob/main/PKGBUILD
sudo apt install gperf
libseccomp_ver="2.6.1"
wget -nv https://github.com/seccomp/libseccomp/releases/download/v${libseccomp_ver}/libseccomp-${libseccomp_ver}.tar.gz
tar -xf libseccomp-*.tar.gz
rm libseccomp-*.tar.gz
root_dir=$(pwd)
cd libseccomp-*
python -m pip install -U pip
python -m pip install Cython setuptools build wheel
./configure --prefix=/usr
make -j
libseccomp_dir=$(pwd)
cd src/python
VERSION_RELEASE=$libseccomp_ver CPPFLAGS="-I${libseccomp_dir}/include" python -m build --wheel --no-isolation
python -m pip install dist/*.whl
cd "$root_dir"
rm -rf libseccomp*

# compile bubblewrap
sudo apt install ninja-build libcap-dev
wget -nv https://github.com/containers/bubblewrap/releases/download/v0.13.1/bubblewrap-0.13.1.tar.xz
tar -xf bubblewrap-*.tar.xz
rm bubblewrap-*.tar.xz
cd bubblewrap-*
python -m pip install meson
meson setup build -Dassume_kernel="$(uname -r | grep -oP '^\d+(\.\d+){2}')"
meson compile -C build
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
