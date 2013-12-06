%define major 1
%define libname	%mklibname x86emu %{major}
%define devname	%mklibname x86emu -d

Summary:	A small x86 emulation library
Name:		libx86emu
License:	BSD 3-Clause
Group:		System/Libraries
URL:		http://gitorious.org/x86emu/libx86emu
Version:	1.3
Release:	5
Source0:	%{name}-%{version}.tar.lzma
ExclusiveArch:	%{ix86} x86_64

%description
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n     %{libname}
Summary:	A small x86 emulation library
Group:		System/Libraries
%description -n %{libname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n     %{devname}
Summary:	A small x86 emulation library
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%prep
%setup -q

%build
%make CFLAGS="%{optflags} -fPIC"

%install
%makeinstall_std LIBDIR=%{_libdir}

%files -n %{libname}
%{_libdir}/libx86emu.so.%{major}*

%files -n %{devname}
%doc README LICENSE
%{_libdir}/*.so
%{_includedir}/x86emu.h

