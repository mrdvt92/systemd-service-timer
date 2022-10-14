Name:      systemd-service-timer
Summary:   systemd-service-timer
Version:   0.02
Release:   1%{?dist}
License:   perl
Group:     System Environment/Daemons
URL:       http://linux.davisnetworks.com/
Source0:   http://linux.davisnetworks.com/%{name}-%{version}.tar.gz
Requires:  perl(DateTime)
Requires:  systemd
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description 
systemd-service-timer

%prep
%setup -q

%build

%install
rm -rf                   $RPM_BUILD_ROOT
mkdir -p                 $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp %{name}.pl            $RPM_BUILD_ROOT/%{_datadir}/%{name}/
mkdir -p                 $RPM_BUILD_ROOT/%{_unitdir}/
cp %{name}.service       $RPM_BUILD_ROOT/%{_unitdir}/
cp %{name}.timer         $RPM_BUILD_ROOT/%{_unitdir}/

%post
systemctl daemon-reload
systemctl enable  %{name}.service
systemctl enable  %{name}.timer

%files
%dir %attr(0755,root,root) %{_datadir}/%{name}/
%attr(0755,root,root) %{_datadir}/%{name}/%{name}.pl
%attr(0644,root,root) %{_unitdir}/%{name}.service
%attr(0644,root,root) %{_unitdir}/%{name}.timer

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
