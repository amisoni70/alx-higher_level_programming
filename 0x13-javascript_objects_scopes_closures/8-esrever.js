#!/usr/bin/node
// Function that returns the reversed version of a list

exports.esrever = function (list) {
  const revList = [];
  const end = list.length - 1;
  for (let k = end; k >= 0; k--) {
    revList.push(list[k]);
  }
  return (revList);
};
