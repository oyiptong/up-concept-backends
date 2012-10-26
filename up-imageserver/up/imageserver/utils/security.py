# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import cef
import tornado.web

class CEFRequestHandler(tornado.web.RequestHandler):

    """
    Handler that relays all unhandled methods to CEF logging. Expects the
    application to have a cef_settings variable that contains something
    similar to:

      {
        "product": "up-imageserver",
        "vendor": "Mozilla",
        "version": 0,
        "device_version": 0,
        "file": "/tmp/cef.log"
      }
    """

    def log_cef(self, name, severity, *args, **kwargs):
        cef_settings = self.application.__dict__.get('cef_settings')
        if cef_settings:
            c = {'cef.product': cef_settings.get("product"),
                 'cef.vendor': cef_settings.get("vendor"),
                 'cef.version': cef_settings.get("version"),
                 'cef.device_version': cef_settings.get("device_version"),
                 'cef.file': cef_settings.get("file")}
            env = { 'REQUEST_METHOD': self.request.method,
                    'PATH_INFO': self.request.uri,
                    'HTTP_HOST': self.request.host,
                    'HTTP_USER_AGENT': self.request.headers.get('User-Agent', '') }
            return cef.log_cef(name, severity, env, *args, config=c, **kwargs)

    def _handle_request(self):
        if self.__class__ == CEFRequestHandler:
            self.log_cef("Unknown handler called", 3)
            self.send_error(404)
        else:
            self.log_cef("Known handler called with unsupported method", 3)
            self.send_error(405)

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self._handle_request()

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        self._handle_request()

    @tornado.web.asynchronous
    def head(self, *args, **kwargs):
        self._handle_request()

    @tornado.web.asynchronous
    def put(self, *args, **kwargs):
        self._handle_request()

    @tornado.web.asynchronous
    def options(self, *args, **kwargs):
        self._handle_request()        
