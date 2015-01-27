#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libaio
Version  : 0.3.110
Release  : 8
URL      : https://fedorahosted.org/releases/l/i/libaio/libaio-0.3.110.tar.gz
Source0  : https://fedorahosted.org/releases/l/i/libaio/libaio-0.3.110.tar.gz
Summary  : Linux-native asynchronous I/O access library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libaio-lib
Patch1: 0001.patch
Patch2: test.patch

%description
The Linux-native asynchronous I/O facility ("async I/O", or "aio") has a
richer API and capability set than the simple POSIX async I/O facility.
This library, libaio, provides the Linux-native API for async I/O.
The POSIX async I/O facility requires this library in order to provide
kernel-accelerated async I/O capabilities, as do applications which
require the Linux-native async I/O API.

%package dev
Summary: dev components for the libaio package.
Group: Development
Requires: libaio-lib
Provides: libaio-devel

%description dev
dev components for the libaio package.


%package lib
Summary: lib components for the libaio package.
Group: Libraries

%description lib
lib components for the libaio package.


%prep
%setup -q -n libaio-0.3.110
%patch1 -p1
%patch2 -p1

%build
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make partcheck || :

%install
rm -rf %{buildroot}
%make_install destdir=%{buildroot} includedir=%{_includedir} libdir=/lib usrlibdir=%{_libdir}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
