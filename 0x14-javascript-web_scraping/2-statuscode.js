#!/usr/bin/node

// import request  module
const request = require('request');

request.get(process.argv[2]).on('response', function(response) {
  console.log('code: ', response.statusCode);
});
