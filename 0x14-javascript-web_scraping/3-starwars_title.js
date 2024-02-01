#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(URL, function (err, res, body) {
  if (err || res.statusCode !== 200) return;
  const data = JSON.parse(body);
  console.log(data.title);
});
