%define major 3
%define libname %mklibname x86emu %{major}
%define devname %mklibname x86emu -d
%define debug_package %{nil}

Summary:	A small x86 emulation library
Name:		libx86emu
License:	BSD 3-Clause
Group:		System/Libraries
URL:		https://github.com/wfeldt/libx86emu
Version:	3.1
Release:	1
Source0:	https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz

%description
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n %{libname}
Summary:	A small x86 emulation library
Group:		System/Libraries

%description -n %{libname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n %{devname}
Summary:	A small x86 emulation library
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%prep
%autosetup -p1

%build
echo %{version} > VERSION
%set_build_flags
%make_build CFLAGS="%{optflags} -fPIC" shared

%install
%make_install LIBDIR=%{_libdir}

%files -n %{libname}
%{_libdir}/libx86emu.so.%{major}*

%files -n %{devname}
%doc README LICENSE
%{_libdir}/*.so
%{_includedir}/x86emu.h
