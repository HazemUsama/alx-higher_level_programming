#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const num = args.map(Number);
  num.sort((a, b) => b - a);
  console.log(num[1]);
}
