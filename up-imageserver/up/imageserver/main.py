#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import json
import logging
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options
import up.imageserver
from up.imageserver import settings
from up.imageserver.urls import routes

class SettingsObj(object):
    def __init__(self, **settings):
        self.__dict__.update(settings)

define("port", help="run on the given port", type=int)
define("address", help="bind to the given address", type=str)
define("num_workers", help="run with the given number of workers. 0 is auto", type=int)
define("config", default="", help="load from a given file instead of the system-wide /etc/up/imageserver.json", type=str)

def main():
    tornado.options.parse_command_line()

    sys_settings = None
    if os.path.isfile('/etc/up/imageserver.json') or options.config:
        if options.config and os.path.isfile(options.config):
            config_file = open(options.config)
        else:
            config_file = open('/etc/up/imageserver.json')
        config = json.load(config_file)
        config_file.close()

        if config.get('imageserver', ''):
            sys_settings = SettingsObj(**config.get('imageserver'))
            settings.server['port'] = sys_settings.server['port']
            settings.server['address'] = sys_settings.server['address']
            settings.server['num_workers'] = sys_settings.server['num_workers']

    if options.port:
        settings.server['port'] = options.port
    if options.num_workers:
        settings.server['num_workers'] = options.num_workers
    if options.address:
        settings.server['address'] = options.address

    application = up.imageserver.UpImageserverAPI(sys_settings if sys_settings else settings, routes)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(port=settings.server.get('port', 5500), address=settings.server.get('address', '127.0.0.1'))

    if settings.application.get('debug', False):
        num_workers = 1
    else:
        num_workers = settings.server.get('num_workers', 0)
    http_server.start(num_workers)

    logging.info("starting server listening on port: {0}".format(settings.server.get('port', 5500)))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
