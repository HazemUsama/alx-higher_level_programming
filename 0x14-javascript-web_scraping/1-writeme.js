#!/usr/bin/node

// import file system module
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  if (error) console.log(error);
});