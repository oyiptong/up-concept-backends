var fs = require('fs');
var os = require('os');

var options = require('commander');

// Command-line parsing
var packageInfo = JSON.parse(fs.readFileSync('./package.json', 'utf8'));
options.version(packageInfo.version)
    .option('-U, --user [value]', 'mongodb username')
    .option('-P, --password [value]', 'mongodb password')
    .option('-D, --database [value]', 'mongodb database')
    .option('-H, --host [value]', 'mongodb host')
    .option('-p, --port <n>', 'mongodb port', parseInt)
    .parse(process.argv);

server = {
    "serverPort": process.env.VCAP_APP_PORT || 5500,
    "numCPUs": os.cpus().length
};

app = {
    "imageUrlPrefix": "https://sitesuggest.mozillalabs.com/images/cars/"
}

if(process.env.VCAP_SERVICES) {
    var env = JSON.parse(process.env.VCAP_SERVICES);
    var mongo = env['mongodb-1.8'][0]['credentials'];
} else {
    var mongo = {
        "hostname": options.host || "localhost",
        "port": options.port || 27017,
        "username": options.user || "",
        "password": options.password || "",
        "db": options.database || "up_suggest"
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
