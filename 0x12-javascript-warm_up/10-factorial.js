#!/usr/bin/node

function fact (n) {
  if (isNaN(n) || n === 1) return 1;
  return fact(n - 1) * n;
}

const arg = process.argv;
const n = parseInt(arg[2]);
console.log(fact(n));
