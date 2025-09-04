%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           edpm-image-builder
Summary:        Builder of edpm required images
Version:        XXX
Release:        XXX
License:        Apache-2.0
Group:          System Environment/Base
URL:            https://github.com/openstack-k8s-operators/edpm-image-builder/
Source0:        https://github.com/openstack-k8s-operators/edpm-image-builder/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  pyproject-rpm-macros

Requires:       diskimage-builder >= 3.24.0
Requires:       openstack-ironic-python-agent-builder

%description
This package contains elements and files needed to build OS images for deploying EDPM bare
metal nodes and ironic-python-agent image which is used by ironic for BMAAS using
diskimage-builder.

%prep
%autosetup -n %{name}-%{upstream_version} -S git

# We are not using automatic requiremens for this package
# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/edpm_image_builder*
%{_datadir}/edpm-image-builder
%{_bindir}/block-device-yaml

%changelog
# REMOVEME: error caused by commit https://github.com/openstack-k8s-operators/edpm-image-builder/commit/0753302c26bc3123be82afa517c6ddc74b50a966
