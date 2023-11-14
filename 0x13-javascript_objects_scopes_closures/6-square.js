#!/usr/bin/node

const BaseSquare = require("./6-square");

class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) c = 'X';
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }

module.exports = BaseSquare;
