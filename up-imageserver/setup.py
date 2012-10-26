# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from setuptools import setup

requires = [
        'tornado==2.4',
        'cef==0.3'
]

setup(name="up.imageserver",
      version="1.0",
      description="API server for serving images based on profile preferences",
      url="https://sitesuggest.mozillalabs.com/",
      author="Mozilla Labs",
      author_email="labs@mozilla.com",
      packages=['up', 'up.imageserver', 'up.imageserver.handlers', 'up.imageserver.utils'],
      namespace_packages=['up'],
      include_package_data=True,
      install_requires = requires,
      scripts=['scripts/up-imageserver-server']
)
