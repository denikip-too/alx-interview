#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const films = 'https://swapi-api.hbtn.io/api/films/';
const movieCharacters = `${films}${process.argv[2]}/`;
request(movieCharacters, function (error, response) {
  if (!error && response.status === 200) {
    return response.json();
  }
  const characters = [];
  for (const key in response) {
    if (key === 'characters') {
      console.log(`${characters[key]}`);
    }
  }
});
