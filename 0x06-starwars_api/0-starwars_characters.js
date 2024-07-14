#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, { json: true }, (err, res, body) => {
  if (err) return;
  print(body.characters, 0);
});
const print = (characters, i) => {
  if (i === characters.length) return;
  request(characters[i], { json: true }, (err, res, body) => {
    if (err) return;
    console.log(body.name);
    print(characters, i + 1);
  });
};
