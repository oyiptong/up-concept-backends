var os = require("os");
var util = require('util');
var handlerUtil = require('./utils.js');

function test(request, response) {
        handlerUtil.respond(response, 200, {"msg": util.format("Listening on %s on machine %s pid %s", request.headers.host, os.hostname(), process.pid)});
}

exports.test = test;
