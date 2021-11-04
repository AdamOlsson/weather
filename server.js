const http = require('http');
const fs = require('fs');

const data_file = "/home/pi/projects/weather/config.json"

const HTTP_GET = "GET"
 
const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
    switch (req.method) {
        case HTTP_GET:
            handleGet(req, res);
            break;
        default:
            console.log("Recevied bad request.");
            res.statusCode = 501;
            res.setHeader('Content-Type', 'text/plain');
            res.end('Not yet implemented.\n');        
            break
    }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});


function handleGet(req, res) {
    let rawdata = fs.readFileSync('data.json');
    let weatherdata = JSON.parse(rawdata);

    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.end(JSON.stringify(weatherdata))
    
}