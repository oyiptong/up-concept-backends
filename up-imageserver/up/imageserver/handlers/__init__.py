# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__import__('pkg_resources').declare_namespace(__name__)
from up.imageserver import UpImageserverAPI

from up.imageserver.utils.security import CEFRequestHandler

class ImageserverHandler(CEFRequestHandler):

    def __init__(self, *args, **kwargs):
        super(ImageserverHandler, self).__init__(*args, **kwargs)
        self.set_header('Content-Type', 'application/json')
        self.add_header('Cache-Control', 'private')

    def return_error(self, message, status=404):
        #TODO log this?
        self.set_status(status)
        self.write(message)
        self.finish()
