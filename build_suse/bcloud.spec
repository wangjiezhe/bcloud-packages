#
# spec file for package bcloud
#
# Released by qgymib <qgymib@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via 
#

# the {_libdir} can not be used under x64
%define python3_sitelib /usr/lib/python3.3/site-packages

Name:           bcloud
Version:        2.2.3
Release:        1.suse
License:        GPL-3.0
Summary:        Baidu Pan client for Linux Desktop users
Url:            https://github.com/LiuLang/bcloud
Group:          Productivity/Networking/Web/Frontends
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       python3
Requires:       python3-base
Requires:       python3-gobject
Requires:       python3-urllib3 >= 1.8
Requires:       python3-keyring >= 3.7
Requires:       sqlite3
Requires:       gnome-icon-theme-symbolic
Obsoletes:      %{name} < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bcloud 是百度网盘的Linux桌面客户端实现.
现在只写了一部分主要功能, 其它功能还要等有空再加入.
gloud 还处于早期的开发阶段, 欢迎各位朋友提交问题.


%prep
%setup -q

%build
# this python module shouldn't be compiled
# we will place all the files to right position

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
cp -r share/ %{buildroot}%{_datadir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc LICENSE README.md HISTORY
%{python3_sitelib}/*
%{_datadir}/icons/*
%{_datadir}/bcloud/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Mar 26 2014 qgymib <usrmib@163.com> 2.2.2-1.suse
- Using keyring to encrypt account password
- Support status icon

* Wed Mar 26 2014 qgymib <usrmib@163.com> 2.2.3-1.suse
- Fixed: saving download status when terminated
- Automatically update user profile
- Support restroing files in Trash
- Add more comments to README
