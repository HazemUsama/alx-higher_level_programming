#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(URL, function (err, res, body) {
  if (err || res.statusCode !== 200) return;
  const films = JSON.parse(body);
  films.characters.forEach(characterURL => {
    request(characterURL, function (err, res, body) {
      if (err || res.statusCode !== 200) return;
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
