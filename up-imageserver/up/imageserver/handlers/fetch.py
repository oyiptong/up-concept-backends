# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import time
import json

from up.imageserver.handlers import ImageserverHandler
import tornado.web as web
import tornado.gen as gen

class FetchRequestHandler(ImageserverHandler):

    @web.asynchronous
    @gen.engine
    def post(self):
        """
        From a json query, return a collection of images that would reflect the preferences given.

        Example input:
        {
            "interests": {
                "automobiles": {
                    "small": {
                        "corolla": true, 
                        "civic": true
                    }, 
                    "asian": {
                        "honda": true, 
                        "toyota": true
                    }
                }, 
                "demographics": {
                    "gender": "male", 
                    "age": "45_55"
                }
        }

        Example output:

        {
            "images": {
                "cause": [
                    "small cars", 
                    "asian", 
                    "male"
                ], 
                "urls": [
                    "http://foo.com/foo.jpg", 
                    "http://foo.com/bar.jpg"
                ]
            }
        }

        """
        try:
            data = json.loads(self.request.body)
        except ValueError:
            raise web.HTTPError(400)

        output = {
                "images": {
                    "cause": [
                        "small cars", 
                        "asian", 
                        "male"
                    ], 
                    "urls": [
                        "http://foo.com/foo.jpg", 
                        "http://foo.com/bar.jpg"
                    ]
                }
        }
        self.write(json.dumps(output))
        self.finish()
