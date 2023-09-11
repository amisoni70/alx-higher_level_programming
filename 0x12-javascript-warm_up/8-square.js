#!/usr/bin/node
// Sqaure

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let k = 0; k < size; k++) {
    let row = '';
    for (let m = 0; m < size; m++) row += 'X';
    console.log(row);
  }
}
