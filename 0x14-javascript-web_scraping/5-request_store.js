#!/usr/bin/node

// import file system module
const fs = require('fs');
const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err || res.statusCode !== 200) return;

  fs.writeFile(process.argv[3], body, 'utf8', error => {
    if (error) throw error;
  });
});
