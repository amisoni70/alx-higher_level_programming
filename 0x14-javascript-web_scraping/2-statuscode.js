#!/usr/bin/node
// A script that dislays the status code of a GET request.

const url = process.argv[2];
const request = require('request');

request(url, function (error, body, response) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
