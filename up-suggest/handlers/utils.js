function respond(response, statusCode, data, pretty) {
    response.writeHead(statusCode, {"Content-Type": "application/json", "Vary": "Interest", "Cache-Control": "private"});
    if(pretty == true) {
        response.write(JSON.stringify(data, null, 4));
    } else {
        response.write(JSON.stringify(data));
    }
    response.end();
}

exports.respond = respond;
