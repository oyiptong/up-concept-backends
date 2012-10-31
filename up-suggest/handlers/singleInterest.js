var handlerUtil = require('./utils.js');

function suggest(request, response) {
    var interest = request.headers.interest;
    if (interest == null) {
        handlerUtil.respond(response, 400, {"err": "interest not specified"});
    }

    handlerUtil.respond(response, 200, {"d": ["http://static.ddmcdn.com/gif/how-to-solve-cat-behavior-problems-2.jpg"]});
}

exports.suggest = suggest;
