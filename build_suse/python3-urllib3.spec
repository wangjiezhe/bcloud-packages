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

%define python3_sitelib /usr/lib/python3.3/site-packages

Name:           python3-urllib3
Version:        1.8
Release:        1.suse
License:        MIT
Summary:        HTTP library with thread-safe connection pooling, file post, and more.
Url:            https://pypi.python.org/pypi/urllib3
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-base
Obsoletes:      %{name} < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
HTTP library with thread-safe connection pooling, file post, and more.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGES.rst README.rst LICENSE.txt
%{python3_sitelib}/*
%exclude %{python3_sitelib}/urllib3/__pycache__

%changelog
* Wed Mar 26 2014 qgymib <usrmib@163.com> 1.8-1.suse
- Packaged by qgymib
