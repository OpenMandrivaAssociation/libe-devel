%define name	libe-devel
%define	version	0.2.2
%define release	%mkrel 9
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

