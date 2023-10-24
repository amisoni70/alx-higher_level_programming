#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches an int.

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
