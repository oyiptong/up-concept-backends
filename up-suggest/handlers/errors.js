var handlerUtil = require('./utils.js');

function notFound(request, response) {
    handlerUtil.respond(response, 404, JSON.stringify({"err": "page not found"}));
}

exports.notFound = notFound;
