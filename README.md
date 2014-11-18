
#ABOUT
这个项目只包含[bcloud](https://github.com/LiuLang/bcloud)的安装包,
以方便各位朋友使用.

请在下载到安装包之后, 先检验一下包的完整性. 有可能会下载的不完整, 最近至少
有两位朋友遇到了这类问题. 可以使用 `$ md5sum bcloud-x.x.x` 来计算下载的安装
包的MD5值, 与 [checksum.txt](checksum.txt) 里面的文件MD5值比较, 如果匹配就
没有问题.

#Debian 安装指南
Debian及基于Debian的发行版(比如ubuntu, linuxmint)请直接下载
bcloud-x.x.x.deb这个包, 然后双击deb包就能安装了;

有些用户并没有安装apt包管理器的GUI界面, 也可以在终端里面安装:

```sh
$ sudo dpkg -i bcloud-x.x.x.deb
$ sudo apt-get -f install
```

#Debian 7 安装指南
Debian 7里面有一个软件包需要手动升级到较新版, `# pip3 install --upgrade keyring`

#Ubuntu 12.04 安装指南
由于ubuntu12.04里面的包非常旧, 在把bcloud的deb包安装好之后, 并不能直接使用,
会出现类似于[issue65](https://github.com/LiuLang/bcloud/issues/65)中的错误,
需要手动更新一下里面的两个模块, 下面的介绍是以新安装的ubuntu12.04.5为基础的:

1.更新软件包索引: `$ sudo apt-get update`

2.安装python3-dev, 在安装python3-crypto时有用: `$ sudo apt-get install python3-dev`

3.安装pip3, 如果你之前没有安装的话: `$ sudo apt-get install python3-setuptools; $ sudo easy_install3 pip`

4.更新python3-crypto到v2.6.1, 因为ubuntu系统里面的是v2.4, 里面的RSA模块功能不
完整: `$ sudo pip3 install --upgrade pycrypto`

5.更新python3-keyring到v4.0, ubuntu系统里的是v0.7: `$ sudo pip3 install --upgrade keyring`

更新好这些组件之后, bcloud就可以正常使用了.


#Fedora 安装指南
执行以下命令安装 bcloud, 目前支持 fc19, fc20, fc21, fc22 :

```sh
# yum install dnf-plugins-core
# dnf copr enable mosquito/myrepo
# dnf install bcloud
```

或者直接到 [myrepo](http://copr.fedoraproject.org/coprs/mosquito/myrepo/) 下载对应的
repo 文件放到 /etc/yum.repos.d/ 中, 然后运行

```sh
# yum install bcloud
```

打包脚本在 build\_rpm 里.

#RHEL 7 安装指南
RHEL / CentOS 7 使用如下命令安装 bcloud:

```sh
# yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-epel-$(rpm -E %?rhel).repo
# yum localinstall http://li.nux.ro/download/nux/dextop/el$(rpm -E %rhel)/x86_64/nux-dextop-release-0-2.el$(rpm -E %rhel).nux.noarch.rpm
# yum install bcloud
```

#OpenSuSE 安装指南
**BCloud现在在OpenSuSE中文源中也可用啦。若您添加了`opensuse_zh`源，可直接在源中搜索`bcloud`，跳过下面的步骤(版本可能更老)**

+ [1 Click Install for 13.1](http://software.opensuse.org/ymp/home:qgymib/openSUSE_13.1/bcloud.ymp?base=openSUSE%3A13.1&query=bcloud)
+ [1 Click Install for 13.2](http://software.opensuse.org/ymp/home:qgymib/openSUSE_13.2/bcloud.ymp?base=openSUSE%3A13.2&query=bcloud)
+ [1 Click Install for Tumbleweed](http://software.opensuse.org/ymp/home:qgymib/openSUSE_Tumbleweed/bcloud.ymp?base=openSUSE%3AFactory&query=bcloud)
+ [1 Click Install for Factory](http://software.opensuse.org/ymp/home:qgymib/openSUSE_Factory/bcloud.ymp?base=openSUSE%3AFactory&query=bcloud)
+ (不推荐)手动安装：请先安装`python3-keyring.suse.rpm`, 再安装`bcloud.suse.rpm`
+ **注意事项**:
    + 使用`1 Click Install`安装方式，您以后可以直接从包管理器获得最近更新
    + Git repo中的rpm包对应的opensuse版本是13.1

#Arch Linux 安装指南

+ 使用 pacman 直接安装 [bcloud](https://www.archlinux.org/packages/community/any/bcloud/) 。
+ 命令示例：

```sh
$ sudo pacman -Syu (或者 sudo pacman -Syy，如果愿意的话)
$ sudo pacman -S bcloud
```

+ **注意事项**:
    + 如果发现 [bcloud](https://www.archlinux.org/packages/community/any/bcloud/) 并非最新版本，请访问 [Flag Package: bcloud](https://www.archlinux.org/packages/community/any/bcloud/flag/) 页面报告问题，官方维护者将会尽快更新至最新版本。
    + Arch用户需要手动配置gnome-keyring, 请阅读这两篇文章:[GNOME_Keyring](https://wiki.archlinux.org/index.php/GNOME_Keyring), [GnomeKeyring#Automatic_Unlocking](https://wiki.gnome.org/action/show/Projects/GnomeKeyring?action=show&redirect=GnomeKeyring#Automatic_Unlocking)

#Gentoo 安装指南
可下载build_gentoo里的ebuild安装，也可下载bcloud-x.x.x.tbz2包安装. 使用中有任何问题请联系 MJsaka <qiuxuenan@gmail.com>. 

另外 bcloud 已经被收录到[Gentoo-zh](https://github.com/microcai/gentoo-zh)
仓库中, 有问题可联系[Liangzhaostrive@gmail.com](Liangzhaostrive@gmail.com).


#依赖关系
如果需要手动安装的话, 也可以用`pip3`(ArchLinux里面是`pip`)来安装,
比如: `# pip3 install bcloud`

需要包含这些软件包:

* gir1.2-gtk-3.0
* gir1.2-notify-0.7
* gnome-icon-theme-symbolic Gnome3 提供的一套按钮图标
* gnome-keyring或者kwalletmanager, 用于托管用户密码
* libgtk-3.0
* libnotifiy4
* notification-daemon
* python3-crypto  使用RSA算法加密用户密码
* python3-cssselect CSS3 属性选择器, 在[这里](https://pypi.python.org/pypi/cssselect)
* python3-dbus  dbus的python3绑定
* python3-gi  Gtk3 的 python3 绑定
* python3-keyring  这个模块是推荐安装的, 用于把帐户的密码存放到gnome-keyring或
kwallet里面
* python3-lxml 强大的XML解析器, 可以在[这里](https://pypi.python.org/pypi/lxml)下载
