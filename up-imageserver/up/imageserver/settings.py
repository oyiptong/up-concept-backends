# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

server = {
        'num_workers' : 0,
        'port' : 5500,
        'address' : "0.0.0.0",
}

application = {
        'debug' : True,
        'gzip' : True,
        'proxy' : {
            #'proxy_host' : 'localhost',
            #'proxy_port' : 8888,
        },
}
