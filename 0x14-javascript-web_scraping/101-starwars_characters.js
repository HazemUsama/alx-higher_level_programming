#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(URL, async (err, res, body) => {
  if (err || res.statusCode !== 200) return;
  const films = JSON.parse(body);
  for (const characterURL of films.characters) {
    await new Promise((resolve, reject) => {
      request(characterURL, function (err, res, body) {
        if (err || res.statusCode !== 200) reject(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
