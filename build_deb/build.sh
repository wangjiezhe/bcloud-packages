#!/bin/sh

# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>

# Use of this source code is governed by GPLv3 license that can be found
# in the LICENSE file.

# v1.1 - 2014.3.26
# Fixed: `Installed-sized'
# v1.0 - 2014.3.19
# project inited.

SRC="../../bcloud"

if [ -d 'fakeroot' ]; then
	rm -rvf fakeroot
fi

PYLIB='fakeroot/usr/lib/python3/dist-packages/'

mkdir -vp fakeroot/usr/bin fakeroot/DEBIAN $PYLIB

cp -v "$SRC/bcloud-gui" fakeroot/usr/bin/
cp -rvf "$SRC/bcloud" $PYLIB/
cp -rvf "../../cssselect/cssselect" $PYLIB/
cp -rvf "$SRC/share" fakeroot/usr/share
find fakeroot -type d -iname '__pycache__' | xargs rm -rf

# Update package size.
usrSize=$(du -s fakeroot/usr | awk '{print $1}')
echo "usrSize is $usrSize"
sed -i "s/Installed-Size: .*$/Installed-Size: $usrSize/" control
cp -vf control fakeroot/DEBIAN/
