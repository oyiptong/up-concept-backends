function respond(response, statusCode, data) {
    response.writeHead(statusCode, {"Content-Type": "application/json", "Vary": "Interest"});
    response.write(JSON.stringify(data));
    response.end();
}

exports.respond = respond;
