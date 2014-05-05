# Copyright 1999-2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=5
PYTHON_COMPAT=( python3_3 python3_4 )

DESCRIPTION="Baidu Pan client for Linux Desktop users"
HOMEPAGE="https://github.com/LiuLang/bcloud"
SRC_URI="https://pypi.python.org/packages/source/b/${PN}/${P}.tar.gz"

KEYWORDS="~amd64"
LICENSE="GPL-3"
SLOT="0"
IUSE=" +python_single_target_python3_3 python_single_target_python3_4 keyring"
REQUIRED_USE="${PYTHON_REQUIRED_USE}"

DEPEND="${PYTHON_DEPS}"
RDEPEND="${DEPEND}
	python_single_target_python3_3?
		( dev-lang/python:3.3[sqlite] )
	python_single_target_python3_4?
		( dev-lang/python:3.4[sqlite] )
	dev-python/pygobject:3
	dev-python/dbus-python
	dev-python/urllib3
	x11-themes/gnome-icon-theme-symbolic
	keyring? ( dev-python/keyring )
	"
src_compile() {
	if use python_single_target_python3_3 ; then
		python3.3 setup.py build ;
	elif use python_single_target_python3_4 ; then
		python3.4 setup.py build ;
	fi
}
src_install() {
	if use python_single_target_python3_3 ; then
		python3.3 setup.py install --root=${D} ;
	elif use python_single_target_python3_4 ; then
		python3.4 setup.py install --root=${D};
	fi
}
