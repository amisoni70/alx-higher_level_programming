#!/usr/bin/node
// Function that executes x no. of times

exports.callMeMoby = function (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
};
