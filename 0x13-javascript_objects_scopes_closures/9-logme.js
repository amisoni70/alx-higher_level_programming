#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value

let k = 0;
exports.logMe = function (item) {
  console.log(k + ': ' + item);
  k++;
};
