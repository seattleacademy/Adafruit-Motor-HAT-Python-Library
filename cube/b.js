var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.text({type:"*/*"}));
var spawn = require("child_process").spawn;

app.all('/drive', function(req, res) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    console.log(req.body);
    addr = req.query.addr || 96; //96,97, or 98
    port = req.query.port || 1; //1 or 2
    steps = req.query.steps || 90 //0 to 360
    forward = req.query.forward || 1 //1 or 2
	var process1 = spawn('python',["b.py", addr,port,steps,forward]);
    res.send(req.query);
});

port = 6005;

app.use(express.static(__dirname + '/public'));

var server = http.createServer(app);
server.listen(port);
console.log('listening on port', port)