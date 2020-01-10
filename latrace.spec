%global	aarch64rev .1
Name:           latrace
Version:        0.5.11
Release:        6%{?aarch64rev}%{?dist}
Summary:        LD_AUDIT feature frontend for glibc 2.4+
Group:          Development/Debuggers
License:        GPLv3+

URL:            http://people.redhat.com/jolsa/latrace
Source:         http://people.redhat.com/jolsa/latrace/dl/%{name}-%{version}.tar.bz2
Patch0:		latrace-aarch64-basic-audit.patch
Patch1:		latrace-ppc64le-basic-audit.patch
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le
BuildRequires:  autoconf bison asciidoc xmlto binutils-devel binutils-static

%description
allows you to trace library calls and get their statistics in a
manner similar to the strace utility (syscall tracing)

%prep
%setup -q
%patch0 -p1 -b .aarch64~
%patch1 -p1 -b .ppc64le~

%build
autoconf
%configure
make V=1

%install
make install ROOTDIR=%{buildroot} V=1
chmod 0755 %{buildroot}/%{_libdir}/libltaudit.so.%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README ReleaseNotes TODO COPYING
%config(noreplace)  %{_sysconfdir}/*
%{_libdir}/libltaudit.so.%{version}
%{_bindir}/latrace
%{_bindir}/latrace-ctl
%{_mandir}/man1/*

%changelog
* Sun Sep  7 2014 Jiri Olsa <jolsa@redhat.com> - 0.5.11-6
- latrace-ppcle64-basic-audit.patch: add basic ppc64le LD_AUDIT support.
- Add ppc64le to ExclusiveArch. (BZ#1125756)

* Sat Jul 26 2014 Jiri Olsa <jolsa@redhat.com> - 0.5.11-5.1
- latrace-aarch64-basic-audit.patch: add basic aarch64 LD_AUDIT support.
- Add aarch64 to ExclusiveArch. (BZ#1094501)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.5.11-5
- Mass rebuild 2013-12-27

* Sun Mar 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.11-4
- Enable building on ARM as it's supported, cleanup spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 28 2011 Jiri Olsa <olsajiri@gmail.com> - 0.5.11-0
- updated to new version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Jiri Olsa <olsajiri@gmail.com> 0.5.10-0
- updated to new version

* Thu Aug  5 2010 Jiri Olsa <olsajiri@gmail.com> 0.5.9-0
- updated to new version
- BZ 609860 - adding binutils-static to BuildRequires

* Tue Sep 08 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.7
- updated to new version
- upstream download moved

* Sun Jul 05 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.6-1
- updates based on the Fedora review comments

* Thu Jul 02 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.5-2
- minor updates based on the Fedora review comments

* Sat Jun 13 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.5-1
- initial spec file
