#!/bin/bash
# This shell script is used to build rpm for bcloud
# Released by wangjiezhe <wangjiezhe@gmail.com>

if [ $# -ne 2 ]
then
	echo "Usage: `basename $0` release-number version"
	exit 1
fi

release=`echo $1 | sed 's/\-/\./g'`
version=$2

# Replace these variables by your pathes
GIT=~/Downloads/github/wangjiezhe/bcloud
DEST=~/Downloads/github/wangjiezhe/bcloud-packages

SOURCES=~/rpmbuild/SOURCES
SPECS=~/rpmbuild/SPECS
RPMS=~/rpmbuild/RPMS/noarch

mkdir -p $SOURCES/bcloud-$release
cd $GIT/
cp -vr HISTORY LICENSE README.md setup.py bcloud-gui bcloud po share $SOURCES/bcloud-"$release"
# rm -rf $SOURCES/bcloud-$release/bcloud/__pycache__/

cd $SOURCES/
tar -cvzf bcloud-"$release".tar.gz bcloud-$release
rm -rf bcloud-$release

cd $SPECS/
sed -i -e '/^Version/s/[0-9]+\.[0-9]+\.[0.9]+/$version/' bcloud.spec
sed -i -e '/^Release/s/[0-9]+/$release/' bcloud.spec
rpmbuild -ba bcloud.spec
cp bcloud.spec $DEST/build_rpm/

cd $RPMS/
cp bcloud-"$release"-"$version".fc20.noarch.rpm $DEST/
