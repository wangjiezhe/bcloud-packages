
#ABOUT
这个项目只包含[bcloud](https://github.com/LiuLang/bcloud)的安装包,
以方便各位朋友使用.

请在下载到安装包之后, 先检验一下包的完整性. 有可能会下载的不完整, 最近至少
有两位朋友遇到了这类问题. 可以使用 `$ md5sum bcloud-x.x.x` 来计算下载的安装
包的MD5值, 与 [checksum.txt](checksum.txt) 里面的文件MD5值比较, 如果匹配就
没有问题.

#Debian系列
请直接下载bcloud-x.x.x.deb这个包, 安装时如果系统里面有gdebi的话, 只需要双击
deb包就能安装了; 如果没有的话, 也可以在终端里面安装:

    $ sudo dpkg -i bcloud-x.x.x.deb
    $ sudo apt-get -f install


#Fedora系列
Fedora 20的话, 请直接下载并安装bcloud-x.x..fc20.noarch.rpm, 它会自动解决所有
依赖关系.

#OpenSuSE安装指南
**适用于13.1、Factory以及Tumbleweed**

+ [1 Click Install for 13.1](http://software.opensuse.org/ymp/home:qgymib:bcloud/openSUSE_13.1/bcloud.ymp?base=openSUSE%3A13.1&query=bcloud)
+ [1 Click Install for Tumbleweed](http://software.opensuse.org/ymp/home:qgymib:bcloud/openSUSE_Tumbleweed/bcloud.ymp?base=openSUSE%3A13.1&query=bcloud)
+ [1 Click Install for Factory](http://software.opensuse.org/ymp/home:qgymib:bcloud/openSUSE_Factory/bcloud.ymp?base=openSUSE%3AFactory&query=bcloud)
+ (不推荐)手动安装：请先安装`python3-keyring.suse.rpm`, 再安装`bcloud.suse.rpm`
+ **注意事项**:
    + 使用`1 Click Install`安装方式，您以后可以直接从包管理器获得最近更新

#Archlinux安装

+ 请先从AUR上安装python-keyring, 然后使用bcloud-x.x.x-any.pkg.tar.xz这个包

#Gentoo安装
可下载build_gentoo里的ebuild安装，也可下载bcloud-x.x.x.tbz2包安装. 使用中有任何问题请联系 MJsaka <qiuxuenan@gmail.com>. 

另外 bcloud 已经被收录到[Gentoo-zh](https://github.com/microcai/gentoo-zh)
仓库中, 有问题可联系[Liangzhaostrive@gmail.com](Liangzhaostrive@gmail.com).
