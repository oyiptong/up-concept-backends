var http = require('http');
var cluster = require('cluster');
var os = require('os');
var util = require('util');

var router = require("./router");

const serverPort = 5500;
const numCPUs = os.cpus().length;

function startServer(route) {
    if(cluster.isMaster) {
        cluster.on('exit', function(worker, code, signal) {
            console.log('worker ' + worker.process.pid + ' died. recovering...');
            cluster.fork();
        });

        cluster.on('listening', function(worker) {
            console.log('worker with PID: ' + worker.process.pid + ' started');
        });

        for (var i = 0; i < numCPUs; i++) {
            cluster.fork();
        }
        console.log(util.format("Server is listening on port %s with %s processes", serverPort, numCPUs));
    } else {
        function handleRequest(request, response) {
            route(request, response);
        }
        http.createServer(handleRequest).listen(serverPort);
    }
};

startServer(router.route);
