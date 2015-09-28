#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXau
Version  : 1.0.8
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.bz2
Summary  : X authorization file management libary
Group    : Development/Tools
License  : MIT
Requires: libXau-lib
Requires: libXau-doc
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

%description dev
dev components for the libXau package.


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


%prep
%setup -q -n libXau-1.0.8

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/Xauth.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
