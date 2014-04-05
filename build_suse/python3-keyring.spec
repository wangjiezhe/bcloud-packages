#
# spec file for package 
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           python3-keyring
Version:        3.7
Release:        1.suse
License:        MIT
Summary:        A easy way to access the system keyring service from python
Url:            https://pypi.python.org/pypi/urllib3
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-base
Provides:       python3-keyring-gnome = %{version}
Provides:       python3-keyring-kde = %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      python3-keyring-gnome < %{version}
Obsoletes:      python3-keyring-kde < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Python keyring lib provides a easy way to access the system keyring service from python.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}
# fix non-executable-script issues
chmod a+x %{buildroot}%{python3_sitelib}/keyring/cli.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.rst README.rst CONTRIBUTORS.txt
%{python3_sitelib}/*
%{_bindir}/*
%exclude %{python3_sitelib}/keyring/__pycache__

%changelog
