#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : logilab-common
Version  : 1.2.2
Release  : 21
URL      : http://pypi.debian.net/logilab-common/logilab-common-1.2.2.tar.gz
Source0  : http://pypi.debian.net/logilab-common/logilab-common-1.2.2.tar.gz
Summary  : collection of low-level Python packages and modules used by Logilab projects
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: logilab-common-bin
Requires: logilab-common-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
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

%description bin
bin components for the logilab-common package.


%package python
Summary: python components for the logilab-common package.
Group: Default

%description python
python components for the logilab-common package.


%prep
%setup -q -n logilab-common-1.2.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pytest

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
