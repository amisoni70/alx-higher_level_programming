#!/usr/bin/node
// This function returns the no. of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(a => a === searchElement).length);
};
