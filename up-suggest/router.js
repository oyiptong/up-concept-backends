var url = require('url');
var testHandlers = require('./handlers/test.js');
var errorHandlers = require('./handlers/errors.js');
var singleInterestHandlers = require('./handlers/singleInterest.js');

var routes = {
    '/': testHandlers.test,
    '/suggest/v1/interest': singleInterestHandlers.suggest
}

function route(request, response) {
    var pathname = url.parse(request.url).pathname;
    if (typeof routes[pathname] === 'function') {
        routes[pathname](request, response);
    } else {
        // catch all
        errorHandlers.notFound(request, response);
    }
}

exports.route = route;
