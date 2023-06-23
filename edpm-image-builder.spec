%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order

Name:           edpm-image-builder
Summary:        Builder of edpm required images
Version:        XXX
Release:        XXX
License:        Apache-2.0
Group:          System Environment/Base
URL:            https://github.com/openstack-k8s-operators/edpm-image-builder/
Source0:        https://github.com/openstack-k8s-operators/edpm-image-builder/edpm-image-builder-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

Requires:       diskimage-builder >= 3.24.0
Requires:       openstack-ironic-python-agent-builder

%description
This package contains elements and files needed to build OS images for deploying EDPM bare
metal nodes and ironic-python-agent image which is used by ironic for BMAAS using
diskimage-builder.

%prep
%autosetup -n %{name}-%{upstream_version} -S git

sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
sed -i /^${pkg}.*/d doc/requirements.txt
sed -i /^${pkg}.*/d test-requirements.txt
done
%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/edpm_image_builder*
%{_datadir}/edpm-image-builder

%changelog
