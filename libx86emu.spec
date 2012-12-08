%define major 1
%define libname	%mklibname	x86emu	%{major}
%define develname	%mklibname	x86emu	-d

Name:           libx86emu
License:        BSD 3-Clause
Group:          System/Libraries
Summary:        A small x86 emulation library
Version:        1.1
Release:        4
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



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-3
+ Revision: 662419
- mass rebuild

* Tue Mar 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-2
+ Revision: 647684
- misc spec fixes
- build with %%{optflags}

* Wed Mar 16 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1-1
+ Revision: 645701
- fixed spec errors
- fixed spec errors
- imported package libx86emu

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - drop '.' at end of summary


* Wed Mar 16 2011 mdawkins <mattydaw@gmail.com> 1.1-1-unity2011
- import for Unity
- mdvized

* Wed Jun 10 2009 snwint@suse.de
- avoid that error in future
