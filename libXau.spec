#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXau
Version  : 1.0.8
Release  : 11
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.bz2
Summary  : X authorization file management libary
Group    : Development/Tools
License  : MIT-Opengroup
Requires: libXau-lib
Requires: libXau-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
A Sample Authorization Protocol for X
Overview
The following note describes a very simple mechanism for providing individual
access to an X Window System display.  It uses existing core protocol and
library hooks for specifying authorization data in the connection setup block
to restrict use of the display to only those clients that show that they
know a server-specific key called a "magic cookie".  This mechanism is *not*
being proposed as an addition to the Xlib standard; among other reasons, a
protocol extension is needed to support more flexible mechanisms.  We have
implemented this mechanism already; if you have comments, please send them
to us.

%package dev
Summary: dev components for the libXau package.
Group: Development
Requires: libXau-lib
Provides: libXau-devel

%description dev
dev components for the libXau package.


%package dev32
Summary: dev32 components for the libXau package.
Group: Default
Requires: libXau-lib32

%description dev32
dev32 components for the libXau package.


%package doc
Summary: doc components for the libXau package.
Group: Documentation

%description doc
doc components for the libXau package.


%package lib
Summary: lib components for the libXau package.
Group: Libraries

%description lib
lib components for the libXau package.


%package lib32
Summary: lib32 components for the libXau package.
Group: Default

%description lib32
lib32 components for the libXau package.


%prep
%setup -q -n libXau-1.0.8
pushd ..
cp -a libXau-1.0.8 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/Xauth.h
/usr/lib64/libXau.so
/usr/lib64/pkgconfig/xau.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXau.so
/usr/lib32/pkgconfig/32xau.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXau.so.6
/usr/lib64/libXau.so.6.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXau.so.6
/usr/lib32/libXau.so.6.0.0
