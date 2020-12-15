#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : logilab-common
Version  : 1.8.0
Release  : 70
URL      : https://files.pythonhosted.org/packages/77/62/44b45f96eec452deac401e4cc70d60ac1d5ad8a1844d4845daa8f042ea22/logilab-common-1.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/77/62/44b45f96eec452deac401e4cc70d60ac1d5ad8a1844d4845daa8f042ea22/logilab-common-1.8.0.tar.gz
Summary  : collection of low-level Python packages and modules used by Logilab projects
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: logilab-common-bin = %{version}-%{release}
Requires: logilab-common-license = %{version}-%{release}
Requires: logilab-common-python = %{version}-%{release}
Requires: logilab-common-python3 = %{version}-%{release}
Requires: setuptools
Requires: typing_extensions
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : setuptools

%description
========================
        
        What's this ?
        -------------
        
        This package contains some modules used by different Logilab projects.
        
        It is released under the GNU Lesser General Public License.
        
        There is no documentation available yet but the source code should be clean and
        well documented.

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
Provides: pypi(logilab_common)
Requires: pypi(mypy_extensions)
Requires: pypi(setuptools)
Requires: pypi(typing_extensions)

%description python3
python3 components for the logilab-common package.


%prep
%setup -q -n logilab-common-1.8.0
cd %{_builddir}/logilab-common-1.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603377752
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/logilab-common
cp %{_builddir}/logilab-common-1.8.0/COPYING %{buildroot}/usr/share/package-licenses/logilab-common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/logilab-common-1.8.0/COPYING.LESSER %{buildroot}/usr/share/package-licenses/logilab-common/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
