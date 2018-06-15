#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : logilab-common
Version  : 1.4.1
Release  : 38
URL      : http://pypi.debian.net/logilab-common/logilab-common-1.4.1.tar.gz
Source0  : http://pypi.debian.net/logilab-common/logilab-common-1.4.1.tar.gz
Summary  : collection of low-level Python packages and modules used by Logilab projects
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: logilab-common-bin
Requires: logilab-common-python3
Requires: logilab-common-python
Requires: setuptools
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest

BuildRequires : python3-dev
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

%description bin
bin components for the logilab-common package.


%package python
Summary: python components for the logilab-common package.
Group: Default
Requires: logilab-common-python3

%description python
python components for the logilab-common package.


%package python3
Summary: python3 components for the logilab-common package.
Group: Default
Requires: python3-core

%description python3
python3 components for the logilab-common package.


%prep
%setup -q -n logilab-common-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523563855
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/logilab-pytest

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
