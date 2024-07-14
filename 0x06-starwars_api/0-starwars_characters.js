#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, { json: true }, (err, res, body) => {
  if (err) return;
  body.characters.forEach(url => request(url, { json: true }, (err, res, body) => {
    if (err) return;
    console.log(body.name);
  }));
});
