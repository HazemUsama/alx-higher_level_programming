#!/usr/bin/node

// import file system module
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  console.log(err || data);
});
