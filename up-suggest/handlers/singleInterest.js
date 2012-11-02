var settings = require('../settings.js');
var handlerUtil = require('./utils.js');
var Car = require('../models/car').Car;
var url = require('url');

function suggest(request, response) {

    var interest = request.headers.interest;
    if (interest === null || interest.length === 0) {
        handlerUtil.respond(response, 400, {"err": "interest not specified"});
    }

    var tokens = interest.split('/');
    var url_parts = url.parse(request.url, true);
    var limit = url_parts.query.limit || 20;


    Car.find({'tags': {'$all': tokens}}).limit(limit).exec(function(err, cars) {
        var output = [];

        cars.forEach(function(car){
            output.push({
                "img": settings.app.imageUrlPrefix + car.image_path,
                "meta": car.tags
            });
        });
        handlerUtil.respond(response, 200, {"d": output});
    });
}

exports.suggest = suggest;
