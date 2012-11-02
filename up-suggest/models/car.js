var settings = require('../settings.js');
var mongoose = require('mongoose');
var db = mongoose.connect(settings.mongoUrl);

var carSchema = new mongoose.Schema({
    "model": {"type": String, "index": {"unique": true}},
    "tags": [String],
    "image_path": String
}, {"collection": "car"});

var Car = db.model('car', carSchema);
exports.Car = Car;
