var handlerUtil = require('./utils.js');
var url = require('url');

function notFound(request, response) {

    var url_parts = url.parse(request.url, true);
    var pretty = url_parts.query.pretty == 'true';

    handlerUtil.respond(response, 404, {"err": "page not found"}, pretty);
}

exports.notFound = notFound;
