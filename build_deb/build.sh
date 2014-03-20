#!/bin/sh

# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>

# Use of this source code is governed by GPLv3 license that can be found
# in the LICENSE file.

# v1.0 - 2014.3.19
# project inited.

SRC="../../gcloud"

if [ -d 'fakeroot' ]; then
	rm -rvf fakeroot
fi

PYLIB='fakeroot/usr/lib/python3/dist-packages/'

mkdir -vp fakeroot/usr/bin fakeroot/DEBIAN $PYLIB

cp -v "$SRC/gcloud.py" fakeroot/usr/bin/gcloud
cp -rvf "$SRC/gcloud" $PYLIB/
cp -rvf "$SRC/share" fakeroot/usr/share
find fakeroot -type d -iname '__pycache__' | xargs rm -rf

# Update package size.
usrSize=$(du -s fakeroot/usr | awk '{print $1}')
sed -i "s/Installed-Sized: .*$/Installed-Size: $usrSize/" control
cp -vf control fakeroot/DEBIAN/
