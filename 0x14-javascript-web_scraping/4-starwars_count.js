#!/usr/bin/node

const request = require('request');
let count = 0;

request.get(process.argv[2], function (err, res, body) {
  if (err || res.statusCode !== 200) return;
  const data = JSON.parse(body).results;

  data.forEach(result => {
    result.characters.forEach(character => {
      if (character.endsWith('/18/')) count++;
    });
  });
  console.log(count);
});
