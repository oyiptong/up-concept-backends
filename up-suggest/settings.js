var os = require('os');

server = {
    "serverPort": process.env.VCAP_APP_PORT || 5500,
    "numCPUs": os.cpus().length
};

app = {
    "imageUrlPrefix": "https://sitesuggest.mozillalabs.com/images/cars/"
}

if(process.env.VCAP_SERVICES) {
    var env = JSON.parse(process.env.VCAP_SERVICES);
    var mongo = env['mongodb-2.0'][0]['credentials'];
} else {
    var mongo = {
        "hostname":"localhost",
        "port":27017,
        "username":"",
        "password":"",
        "name":"",
        "db":"up_suggest"
    }
}
var generate_mongo_url = function(obj) {
    obj.hostname = (obj.hostname || 'localhost');
    obj.port = (obj.port || 27017);
    obj.db = (obj.db || 'test');

    if (obj.username && obj.password) {
        return "mongodb://" + obj.username + ":" + obj.password + "@" + obj.hostname + ":" + obj.port + "/" + obj.db;
    } else {
        return "mongodb://" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }
}

var mongoUrl = generate_mongo_url(mongo);

exports.server = server;
exports.app = app;
exports.mongoUrl = mongoUrl;
