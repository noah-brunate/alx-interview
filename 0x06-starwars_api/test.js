#!/usr/bin/node

const request = require('request');


url = 'http https://swapi-api.alx-tools.com/api/films';
response = request.get(url);
dat = response.json();
console.log(dat);
