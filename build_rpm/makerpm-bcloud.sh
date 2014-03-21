#!/bin/bash
# This shell script is used to build rpm for bcloud
# Released by wangjiezhe <wangjiezhe@gmail.com>

if [ $# -ne 1 ]
then
	echo "Usage: `basename $0` release-number"
	exit 1
fi

release=$1
# sed -i 's/\-/\./g' $release

# replace these variables by your pathes
GIT=PATH_TO_YOUR_SOURCE_DIR
SOURCES=~/rpmbuild/SOURCES
SPECS=~/rpmbuild/SPECS


mkdir -p $SOURCES/bcloud-$release
cd $GIT/
cp -vr HISTORY LICENSE README.md setup.py bcloud-gui bcloud po share $SOURCES/bcloud-$release
# rm -rf $SOURCES/bcloud-$release/bcloud/__pycache__/

cd $SOURCES/
tar -cvzf bcloud-"$release".tar.gz bcloud-$release
rm -rf bcloud-$release

cd $SPECS/
rpmbuild -ba bcloud.spec

