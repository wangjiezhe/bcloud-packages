#
# spec file for package bcloud
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


Name:           bcloud
Version:        3.5.1
Release:        0
Summary:        Baidu Pan client for Linux Desktop users
License:        GPL-3.0
Group:          Productivity/Networking/Web/Frontends
Url:            https://github.com/LiuLang/bcloud
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gtk3-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:	update-desktop-files
Requires:       dbus-1-python3
Requires:       girepository-1_0
Requires:       gnome-icon-theme-symbolic
Requires:       gtk3-data >= 3.4.0
Requires:       libnotify4
Requires:       libwebkitgtk3
Requires:       python3
Requires:       python3-cssselect
Requires:       python3-gobject
Requires:       python3-keyring >= 3.7
Requires:       python3-lxml
Requires:       python3-pycrypto
Requires:       sqlite3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Baidu Pan client for Linux Desktop users.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}

rm -rf %{buildroot}%{_datadir}/icons/hicolor/512*
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc LICENSE README.md HISTORY
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%{_datadir}/bcloud
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_bindir}/bcloud-gui

%changelog
