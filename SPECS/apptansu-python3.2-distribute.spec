Summary: distribute for apptansu-python3.2
Name: apptansu-python3.2-distribute
Version: 0.6.25
Release: 1%{?dist}
License: Python
Vendor: Apptansu
Group: Development/Languages
Provides: apptansu-python3.2-distribute
Source: distribute-%{version}.tgz

BuildRequires: apptansu-python3.2
AutoReq: no
AutoProv: no
Requires: apptansu-python3.2

%define _prefix /usr/lib/apptansu

%description
distribute for apptansu-python3.2

%prep
%setup -q -n distribute-%{version}

%build

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# Don't install easy_install, just easy_install-x.y
rm %{buildroot}%{_prefix}/bin/easy_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/*

%changelog
* Sun Feb 05 2012 Apptansu <support@apptansu.com> 0.6.25-1
- Initial packaging.
