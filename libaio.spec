#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libaio
Version  : 0.3.113
Release  : 22
URL      : https://releases.pagure.org/libaio/libaio-0.3.113.tar.gz
Source0  : https://releases.pagure.org/libaio/libaio-0.3.113.tar.gz
Summary  : Linux-native asynchronous I/O access library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libaio-filemap = %{version}-%{release}
Requires: libaio-lib = %{version}-%{release}
Requires: libaio-license = %{version}-%{release}

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


%package filemap
Summary: filemap components for the libaio package.
Group: Default

%description filemap
filemap components for the libaio package.


%package lib
Summary: lib components for the libaio package.
Group: Libraries
Requires: libaio-license = %{version}-%{release}
Requires: libaio-filemap = %{version}-%{release}

%description lib
lib components for the libaio package.


%package license
Summary: license components for the libaio package.
Group: Default

%description license
license components for the libaio package.


%prep
%setup -q -n libaio-0.3.113
cd %{_builddir}/libaio-0.3.113
pushd ..
cp -a libaio-0.3.113 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650419969
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make partcheck || :

%install
export SOURCE_DATE_EPOCH=1650419969
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libaio
cp %{_builddir}/libaio-0.3.113/COPYING %{buildroot}/usr/share/package-licenses/libaio/cf756914ec51f52f9c121be247bfda232dc6afd2
pushd ../buildavx2/
%make_install_v3 destdir=%{buildroot} includedir=%{_includedir} libdir=/lib usrlibdir=%{_libdir}
popd
%make_install destdir=%{buildroot} includedir=%{_includedir} libdir=/lib usrlibdir=%{_libdir}
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/lib/libaio.so
/lib/libaio.so.1
/lib/libaio.so.1.0.2

%files dev
%defattr(-,root,root,-)
/usr/include/libaio.h

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libaio

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libaio/cf756914ec51f52f9c121be247bfda232dc6afd2
