#
#    agent-smtp - XXXX
#
#    Copyright (C) 2014 - 2015 Eaton                                        
#                                                                           
#    This program is free software; you can redistribute it and/or modify   
#    it under the terms of the GNU General Public License as published by   
#    the Free Software Foundation; either version 2 of the License, or      
#    (at your option) any later version.                                    
#                                                                           
#    This program is distributed in the hope that it will be useful,        
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
#    GNU General Public License for more details.                           
#                                                                           
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.            
#

Name:           agent-smtp
Version:        0.1.0
Release:        1
Summary:        xxxx
License:        GPL-2.0+
URL:            https://eaton.com/
Source0:        %{name}-%{version}.tar.gz
Group:          System/Libraries
# Note: ghostscript is required by graphviz which is required by
#       asciidoc. On Fedora 24 the ghostscript dependencies cannot
#       be resolved automatically. Thus add working dependency here!
BuildRequires:  ghostscript
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  systemd
%{?systemd_requires}
BuildRequires:  xmlto
BuildRequires:  gcc-c++
BuildRequires:  zeromq-devel
BuildRequires:  czmq-devel
BuildRequires:  malamute-devel
BuildRequires:  libbiosproto-devel
BuildRequires:  magic-devel
BuildRequires:  cxxtools-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
agent-smtp xxxx.

%package -n libagent_smtp0
Group:          System/Libraries
Summary:        xxxx

%description -n libagent_smtp0
agent-smtp xxxx.
This package contains shared library.

%post -n libagent_smtp0 -p /sbin/ldconfig
%postun -n libagent_smtp0 -p /sbin/ldconfig

%files -n libagent_smtp0
%defattr(-,root,root)
%{_libdir}/libagent_smtp.so.*

%package devel
Summary:        xxxx
Group:          System/Libraries
Requires:       libagent_smtp0 = %{version}
Requires:       zeromq-devel
Requires:       czmq-devel
Requires:       malamute-devel
Requires:       libbiosproto-devel
Requires:       magic-devel
Requires:       cxxtools-devel

%description devel
agent-smtp xxxx.
This package contains development files.

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libagent_smtp.so
%{_libdir}/pkgconfig/libagent_smtp.pc
%{_mandir}/man3/*
%{_mandir}/man7/*

%prep
%setup -q

%build
sh autogen.sh
%{configure} --with-systemd-units
make %{_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

# remove static libraries
find %{buildroot} -name '*.a' | xargs rm -f
find %{buildroot} -name '*.la' | xargs rm -f

%files
%defattr(-,root,root)
%{_bindir}/bios-agent-smtp
%{_bindir}/bios-device-scan
%{_mandir}/man1/bios-agent-smtp*
%{_bindir}/bios-sendmail
%{_mandir}/man1/bios-sendmail*
%config(noreplace) %{_sysconfdir}/agent-smtp/bios-agent-smtp.cfg
/usr/lib/systemd/system/bios-agent-smtp.service
%dir %{_sysconfdir}/agent-smtp
%{_prefix}/lib/tmpfiles.d/bios-agent-smtp.conf


%if 0%{?suse_version} > 1315
%post
%systemd_post bios-agent-smtp.service
%preun
%systemd_preun bios-agent-smtp.service
%postun
%systemd_postun_with_restart bios-agent-smtp.service
%endif

%changelog
