var url = require('url');
var util = require('util');
var os = require("os");

function respond(response, statusCode, data) {
    response.writeHead(statusCode, {"Content-Type": "application/json", "Vary": "Interest"});
    response.write(JSON.stringify(data));
    response.end();
}

// request handlers

function test(request, response) {
        respond(response, 200, {"msg": util.format("Listening on: %s hostname : %s", request.headers.host, os.hostname())});
}

function notFound(request, response) {
    respond(response, 404, JSON.stringify({"err": "page not found"}));
}

function v1_singleInterest(request, response) {
    var interest = request.headers.interest;
    if (interest == null) {
        respond(response, 400, {"err": "interest not specified"});
    }

    respond(response, 200, {"d": ["http://static.ddmcdn.com/gif/how-to-solve-cat-behavior-problems-2.jpg"}]);
}

exports.v1_singleInterest = v1_singleInterest;
exports.test = test;
exports.notFound = notFound;
