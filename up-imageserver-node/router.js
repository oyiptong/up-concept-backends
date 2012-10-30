var url = require('url');
var handlers = require('./handlers.js');

var routes = {
    '/': handlers.test,
    '/suggest/v1/interest': handlers.v1_singleInterest
}

function route(request, response) {
    var pathname = url.parse(request.url).pathname;
    if (typeof routes[pathname] === 'function') {
        routes[pathname](request, response);
    } else {
        // catch all
        handlers.notFound(request, response);
    }
}

exports.route = route;
