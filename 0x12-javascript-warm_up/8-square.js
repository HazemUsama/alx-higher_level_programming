#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
