#!/usr/bin/node
// print all characters of a Star Wars movie

const request = require('request');
const films = 'https://swapi-api.hbtn.io/api/films/';
const movieCharacters = `${films}${process.argv[2]}/`;
request(movieCharacters, function (error, response) {
  if (!error && response.status === 200) {
    return response.json();
  }
  for (const key in response) {
    for (const value in response[key]) {
      if (response[key] === 'characters') {
        console.log(response[key][value]);
      }
    }
  }
});
