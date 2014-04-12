
#ABOUT
这个项目只包含[bcloud](https://github.com/LiuLang/bcloud)的安装包,
以方便各位朋友使用.

#Debian系列
请直接下载bcloud-x.x.x.deb这个包, 安装时如果系统里面有gdebi的话, 只需要双击
deb包就能安装了; 如果没有的话, 也可以在终端里面安装:

    $ sudo dpkg -i bcloud-x.x.x.deb
    $ sudo apt-get -f update

ubuntu 12.04 的系统里没有python3-urllib3这个包, 请下载那个
python3-urllib3-1.3-3-all.deb, 先安装它, 再安装bcloud就可以了.

#Fedora系列
Fedora 20的话, 请直接下载并安装bcloud-x.x..fc20.noarch.rpm, 它会自动解决所有
依赖关系.

#OpenSuSE安装指南
**适用于13.1、Factory以及Tumbleweed**

+ [1 Click Install for 13.1](http://software.opensuse.org/ymp/home:qgymib:bcloud/openSUSE_13.1/bcloud.ymp?base=openSUSE%3A13.1&query=bcloud)
+ [1 Click Install for Tumbleweed](http://software.opensuse.org/ymp/home:qgymib:bcloud/openSUSE_Tumbleweed/bcloud.ymp?base=openSUSE%3A13.1&query=bcloud)
+ [1 Click Install for Factory](http://software.opensuse.org/ymp/home:qgymib:bcloud/openSUSE_Factory/bcloud.ymp?base=openSUSE%3AFactory&query=bcloud)
+ (不推荐)手动安装：请先安装`python3-keyring.suse.rpm`以及`python3-urllib3.suse.rpm`再安装`bcloud.suse.rpm`
+ **注意事项**:
    + 使用`1 Click Install`安装方式，您以后可以直接从包管理器获得最近更新
    + 美化Gtk3程序: 系统设置->应用程序外观->Gtk->选择一个GTK3主题: Zukitwo.
      若没有此主题可以在右下方"获取新主题"->"下载GTK3主题"中获得

#Archlinux安装

+ 请先从AUR上安装python-urllib3和python-keyring
然后使用bcloud-x.x.x-any.pkg.tar.xz这个包

