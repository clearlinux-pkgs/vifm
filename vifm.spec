#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x99DC5E4DB05F6BE2 (xaizek@posteo.net)
#
Name     : vifm
Version  : 0.13
Release  : 6
URL      : https://github.com/vifm/vifm/releases/download/v0.13/vifm-0.13.tar.bz2
Source0  : https://github.com/vifm/vifm/releases/download/v0.13/vifm-0.13.tar.bz2
Source1  : https://github.com/vifm/vifm/releases/download/v0.13/vifm-0.13.tar.bz2.asc
Summary  : A filemanager for the console with VIM like keybindings and control.
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: vifm-bin = %{version}-%{release}
Requires: vifm-data = %{version}-%{release}
Requires: vifm-license = %{version}-%{release}
Requires: vifm-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file-dev
BuildRequires : groff
BuildRequires : ncurses-dev
BuildRequires : util-linux
BuildRequires : vim
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Vifm - Vim-like file manager
2001 - 2023
Version: 0.13
This file last updated: 04 April 2023

%package bin
Summary: bin components for the vifm package.
Group: Binaries
Requires: vifm-data = %{version}-%{release}
Requires: vifm-license = %{version}-%{release}

%description bin
bin components for the vifm package.


%package data
Summary: data components for the vifm package.
Group: Data

%description data
data components for the vifm package.


%package doc
Summary: doc components for the vifm package.
Group: Documentation
Requires: vifm-man = %{version}-%{release}

%description doc
doc components for the vifm package.


%package license
Summary: license components for the vifm package.
Group: Default

%description license
license components for the vifm package.


%package man
Summary: man components for the vifm package.
Group: Default

%description man
man components for the vifm package.


%prep
%setup -q -n vifm-0.13
cd %{_builddir}/vifm-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689750198
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689750198
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vifm
cp %{_builddir}/vifm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/vifm/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/vifm-%{version}/COPYING.3party %{buildroot}/usr/share/package-licenses/vifm/e3cad7c3cdd18837d74164db2b7296a7723ad19d || :
cp %{_builddir}/vifm-%{version}/tests/test-support/stic/LICENSE.txt %{buildroot}/usr/share/package-licenses/vifm/b37afbbf019200f60b8c5324d31a56d97564b165 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vifm
/usr/bin/vifm-convert-dircolors
/usr/bin/vifm-pause
/usr/bin/vifm-screen-split

%files data
%defattr(-,root,root,-)
/usr/share/applications/vifm.desktop
/usr/share/bash-completion/completions/vifm
/usr/share/fish/vendor_completions.d/vifm.fish
/usr/share/icons/hicolor/128x128/apps/vifm.png
/usr/share/icons/hicolor/scalable/apps/vifm.svg
/usr/share/pixmaps/vifm.png
/usr/share/vifm/colors/Default-256.vifm
/usr/share/vifm/colors/astrell-root.vifm
/usr/share/vifm/colors/astrell-user.vifm
/usr/share/vifm/colors/dmilith-root.vifm
/usr/share/vifm/colors/dmilith-user.vifm
/usr/share/vifm/colors/istib-solarized-dark.vifm
/usr/share/vifm/colors/juef-zenburn.vifm
/usr/share/vifm/colors/reicheltd-light.vifm
/usr/share/vifm/vifm-help.txt
/usr/share/vifm/vifm-media
/usr/share/vifm/vifmrc
/usr/share/vifm/vim-doc/doc/tags
/usr/share/vifm/vim-doc/doc/vifm-app.txt
/usr/share/vifm/vim-doc/doc/vifm-lua.txt
/usr/share/vifm/vim/autoload/vifm/colorconv.vim
/usr/share/vifm/vim/autoload/vifm/edit.vim
/usr/share/vifm/vim/autoload/vifm/globals.vim
/usr/share/vifm/vim/doc/tags
/usr/share/vifm/vim/doc/vifm-plugin.txt
/usr/share/vifm/vim/ftdetect/vifm-rename.vim
/usr/share/vifm/vim/ftdetect/vifm.vim
/usr/share/vifm/vim/ftplugin/mail_vifm.vim
/usr/share/vifm/vim/ftplugin/vifm-cmdedit.vim
/usr/share/vifm/vim/ftplugin/vifm-edit.vim
/usr/share/vifm/vim/ftplugin/vifm-rename.vim
/usr/share/vifm/vim/ftplugin/vifm.vim
/usr/share/vifm/vim/plugin/vifm.vim
/usr/share/vifm/vim/syntax/vifm.vim
/usr/share/zsh/site-functions/_vifm

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/vifm/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vifm/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/vifm/b37afbbf019200f60b8c5324d31a56d97564b165
/usr/share/package-licenses/vifm/e3cad7c3cdd18837d74164db2b7296a7723ad19d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/vifm-convert-dircolors.1
/usr/share/man/man1/vifm-pause.1
/usr/share/man/man1/vifm-screen-split.1
/usr/share/man/man1/vifm.1
