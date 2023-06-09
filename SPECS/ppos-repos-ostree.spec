BuildArch:     noarch
Name:          ppos-repos-ostree
Version:       38
Release:       3
License:       GPLv3
Group:         Unspecified
Summary:       OSTree specific files for PhotonPonyOS
Distribution:  PhotonPonyOS

URL:           hhttps://github.com/AP-Sensing/ppos-repos-ostree/tree/ppos38
Vendor:        AP Sensing
Packager:      AP Sensing
Provides:      ppos-repos-ostree = %{version}-%{release}
Requires:      system-release(%{version})
Requires:      ppos-repos == %{version}

Source1: ppos-compose.conf


%description
This package provides ostree repository configurations for PhotonPonyOS.

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/ostree/remotes.d/
install -m 644 %{_sourcedir}/ppos-compose.conf $RPM_BUILD_ROOT/etc/ostree/remotes.d/

%files
%dir %attr(0755, root, root) "/etc/ostree/remotes.d"
%attr(0644, root, root) "/etc/ostree/remotes.d/ppos-compose.conf"

%changelog
* Thu Jun 15 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 38-3
- Fixed changelog order
* Thu Jun 15 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 38-2
- Using https for the repo
* Wed Jun 07 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 38-1
- Initial release
