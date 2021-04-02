%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-firefox
Version: 2.9
Release: alt1

Summary: FireFox-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-firefox
BuildArch: noarch

Source0: policy-templates.tar

%description
Firefox-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy-templates

%install
mkdir -p %buildroot%_datadir
cp -a windows/ %buildroot%_destdir

%files
%dir %_destdir
%_destdir

%changelog
* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 2.9-alt1
- Initial release 

