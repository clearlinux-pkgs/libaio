#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libaio
Version  : 0.3.112
Release  : 19
URL      : http://ftp.debian.org/debian/pool/main/liba/libaio/libaio_0.3.112.orig.tar.xz
Source0  : http://ftp.debian.org/debian/pool/main/liba/libaio/libaio_0.3.112.orig.tar.xz
Summary  : Linux-native asynchronous I/O access library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libaio-lib = %{version}-%{release}
Requires: libaio-license = %{version}-%{release}
Patch1: 0001.patch

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
Requires: libaio-lib = %{version}-%{release}
Provides: libaio-devel = %{version}-%{release}
Requires: libaio = %{version}-%{release}

%description dev
dev components for the libaio package.


%package lib
Summary: lib components for the libaio package.
Group: Libraries
Requires: libaio-license = %{version}-%{release}

%description lib
lib components for the libaio package.


%package license
Summary: license components for the libaio package.
Group: Default

%description license
license components for the libaio package.


%prep
%setup -q -n libaio-0.3.112
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555628804
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make partcheck || :

%install
export SOURCE_DATE_EPOCH=1555628804
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libaio
cp COPYING %{buildroot}/usr/share/package-licenses/libaio/COPYING
%make_install destdir=%{buildroot} includedir=%{_includedir} libdir=/lib usrlibdir=%{_libdir}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libaio.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaio.so.1
/usr/lib64/libaio.so.1.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libaio/COPYING
