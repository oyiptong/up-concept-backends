#!/bin/sh

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

set -x

rm -rf up-imageserver-env

virtualenv --python=python2.7 --no-site-packages up-imageserver-env
. up-imageserver-env/bin/activate

export MOZ_UP_DEV=1

(cd up-imageserver && python setup.py develop)
