#!/bin/bash
# This shell script is used to build rpm for bcloud
# Released by wangjiezhe <wangjiezhe@gmail.com>

if [ $# -ne 2 ]
then
	echo "Usage: `basename $0` version release"
	exit 1
fi

version=`echo $1 | sed "s/-/./g"`
release=$2

# Replace these variables by your pathes
GIT=PATH_TO_YOUR_SOURCE_DIR
DEST=PATH_TO_YOUR_DEST_DIR

SOURCES=~/rpmbuild/SOURCES
SPECS=~/rpmbuild/SPECS
RPMS=~/rpmbuild/RPMS/noarch

mkdir -p $SOURCES/bcloud-"$version"
cd $GIT/
cp -vr HISTORY LICENSE README.md setup.py bcloud-gui bcloud po share $SOURCES/bcloud-"$version"
# rm -rf $SOURCES/bcloud-$version/bcloud/__pycache__/

cd $SOURCES/
tar -cvzf bcloud-"$version".tar.gz bcloud-$version
rm -rf bcloud-$version

cd $SPECS/
sed -i "/^Version/s/[0-9]\+\.[0-9]\+\.[0-9]\+/$version/" bcloud.spec
sed -i "/^Release/s/[0-9]\+/$release/" bcloud.spec
rpmbuild -ba bcloud.spec
cp bcloud.spec $DEST/build_rpm/
# cp makerpm-bcloud.sh $DEST/build_rpm/

cd $RPMS/
cp bcloud-"$version"-"$release".fc20.noarch.rpm $DEST/
