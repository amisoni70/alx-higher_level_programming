#!/usr/bin/node
// script that prints an integer

if (isNaN(process.argv[2])) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
