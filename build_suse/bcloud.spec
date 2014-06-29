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
Version:        3.4.2
Release:        1%{?dist}
License:        GPL-3.0
Summary:        Baidu Pan client for Linux Desktop users
Url:            https://github.com/LiuLang/bcloud
Group:          Productivity/Networking/Web/Frontends
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  gtk3-devel
Requires:       update-desktop-files
Requires:       gtk3-data >= 3.4.0
Requires:       python3
Requires:       python3-base
Requires:       python3-gobject
Requires:       python3-pycrypto
Requires:       python3-cssselect
Requires:       python3-lxml
Requires:       libwebkitgtk3-devel
Requires:       python3-keyring >= 3.7
Requires:       sqlite3
Requires:       gnome-icon-theme-symbolic
Requires:       girepository-1_0
Requires:       libnotify4
Requires:       dbus-1-python3
Obsoletes:      %{name} < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bcloud 是百度网盘的Linux桌面客户端实现.
现在只写了一部分主要功能, 其它功能还要等有空再加入.
bcloud 还处于早期的开发阶段, 欢迎各位朋友提交问题.

%prep
%setup -q

%build
# fix build error in factory version
%if 0%{?suse_version} > 1310
    export XDG_RUNTIME_DIR=/tmp/%{name}
%endif

python3 setup.py build

%install
# {buildroot} should be cleaned before install installation
rm -rf %{buildroot}
# copy executable file to /usr/bin
install -d %{buildroot}%{_bindir}/
install bcloud-gui %{buildroot}%{_bindir}
# copy python module to sitelib
install -d %{buildroot}%{python3_sitelib}
cp -r bcloud/ %{buildroot}%{python3_sitelib}
# copy resources to /usr/share
cp -r share/ %{buildroot}%{_datadir}/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc LICENSE README.md HISTORY
%{python3_sitelib}/*
%{_datadir}/bcloud
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_bindir}/bcloud-gui
%exclude %{python3_sitelib}/bcloud/__pycache__

%changelog
