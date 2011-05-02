%define major 1
%define libname	%mklibname	x86emu	%{major}
%define develname	%mklibname	x86emu	-d

Name:           libx86emu
License:        BSD 3-Clause
Group:          System/Libraries
Summary:        A small x86 emulation library
Version:        1.1
Release:        3
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64

%description
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n     %{libname}
Summary:        A small x86 emulation library
Group:          System/Libraries

%description -n %{libname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%package -n     %{develname}
Summary:        A small x86 emulation library
Group:          System/Libraries
Requires:       %{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%prep
%setup -q

%build
%make CFLAGS="%{optflags} -fPIC"

%install
%makeinstall_std LIBDIR=%{_libdir}

%clean 
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/x86emu.h
%doc README LICENSE

