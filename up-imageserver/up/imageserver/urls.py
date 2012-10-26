# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from up.imageserver.handlers import test
from up.imageserver.handlers import fetch
from up.imageserver.utils.security import CEFRequestHandler

routes = (
        (r'/imageserver/?', test.TestRequestHandler),
        (r'/imageserver/fetch', fetch.FetchRequestHandler),
        (r'.*', CEFRequestHandler)
)
