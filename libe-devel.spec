%define name	libe-devel
%define	version	0.2.2
%define release	%mkrel 11
%define realname libe

Summary:	C library contains various functions which deal with data structures
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other	
URL:		http://www.cs.berkeley.edu/~bnc/libe/
Source:		%{realname}-%{version}.tar.bz2
Provides:	%{name}-%{version}
Provides:	libe-cluster
Conflicts:	libe0-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
libe is a C library which contains various functions which deal with 
data structures (hash tables, bitmasks, trees of IP addresses, etc.), 
networking, I/O, barriers, and other useful things. It is currently used 
in the implementation of authd (RSA authentication daemon), pcp (a 
parallel, pipelined file transfer system), and gexec (a fast, hierarchical 
cluster remote execution system).

%prep
rm -rf ${buildroot}

%setup -q -n %realname-%version

%build

%configure 

%make

%install

%makeinstall

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root) 
%doc INSTALL AUTHORS ChangeLog COPYING
%{_includedir}/e
%{_libdir}/libe.a



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-11mdv2011.0
+ Revision: 620119
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-10mdv2010.0
+ Revision: 429726
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.2.2-9mdv2009.0
+ Revision: 248643
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.2.2-7mdv2008.1
+ Revision: 128551
- kill re-definition of %%buildroot on Pixel's request
- import libe-devel


* Wed Dec 12 2005 Erwan Velu <erwan@seanodes.com> 0.2.2-7mdk
- Conflict with e17

* Fri Jun 10 2004 Erwan Velu <erwan@mandrakesoft.com> 0.2.2-6mdk
- Rebuild

* Sat Feb 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.2.2-5mdk
- Fix DIRM (distlint)

* Fri Jan 03 2003 Antoine Ginies <aginies@mandrakesoft.com> 0.2.2-4mdk
- build for new glibc

* Tue Aug 6 2002 Antoine Ginies <aginies@mandrakesoft.com> 0.2.2-3mdk
- build with gcc 3.2

* Thu Jul 11 2002 Antoine Ginies <aginies@mandrakesoft.com> 0.2.2-2mdk
- Build on 8.2 with 2.96

* Wed May 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.2-1mdk
- add %%realname
- prefix=%%__bindir
- remove useless ldconfig

* Tue Apr 21 2002 Antoine Ginies <aginies@mandrakesoft.com> 0.2.1-1mdk
- first release for Mandrakesoft
