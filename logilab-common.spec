#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : logilab-common
Version  : 1.5.1
Release  : 52
URL      : https://files.pythonhosted.org/packages/80/8b/1e3d38c95f65618c804c975e843da30ac8e55b3e45d07eaf1257cfb6d023/logilab-common-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/8b/1e3d38c95f65618c804c975e843da30ac8e55b3e45d07eaf1257cfb6d023/logilab-common-1.5.1.tar.gz
Summary  : collection of low-level Python packages and modules used by Logilab projects
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: logilab-common-bin = %{version}-%{release}
Requires: logilab-common-license = %{version}-%{release}
Requires: logilab-common-python = %{version}-%{release}
Requires: logilab-common-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : setuptools

%description
Logilab's common library
========================
What's this ?
-------------
This package contains some modules used by different Logilab projects.

%package bin
Summary: bin components for the logilab-common package.
Group: Binaries
Requires: logilab-common-license = %{version}-%{release}

%description bin
bin components for the logilab-common package.


%package license
Summary: license components for the logilab-common package.
Group: Default

%description license
license components for the logilab-common package.


%package python
Summary: python components for the logilab-common package.
Group: Default
Requires: logilab-common-python3 = %{version}-%{release}

%description python
python components for the logilab-common package.


%package python3
Summary: python3 components for the logilab-common package.
Group: Default
Requires: python3-core

%description python3
python3 components for the logilab-common package.


%prep
%setup -q -n logilab-common-1.5.1
cd %{_builddir}/logilab-common-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575279591
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/logilab-common
cp %{_builddir}/logilab-common-1.5.1/COPYING %{buildroot}/usr/share/package-licenses/logilab-common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/logilab-common-1.5.1/COPYING.LESSER %{buildroot}/usr/share/package-licenses/logilab-common/9a1929f4700d2407c70b507b3b2aaf6226a9543c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/pytest

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/logilab-pytest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/logilab-common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/logilab-common/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
