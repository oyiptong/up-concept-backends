# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__import__('pkg_resources').declare_namespace(__name__)
import logging
import socket
import tornado.web

class UpImageserverAPI(tornado.web.Application):
    def __init__(self, settings, routes):
        self.application_settings = settings.application

        self.cef_settings = settings.__dict__.get('cef')
        super(UpImageserverAPI, self).__init__(routes, **settings.application)
        self.hostname = socket.gethostname().replace('.', '_')

        if not hasattr(UpImageserverAPI, '_instance'):
            UpImageserverAPI._instance = self

    @staticmethod
    def instance():
        if hasattr(UpImageserverAPI, '_instance'):
            return UpImageserverAPI._instance
        else:
            raise UpImageserverAPINotInitializedError()

class UpImageserverAPINotInitializedError(Exception): pass
