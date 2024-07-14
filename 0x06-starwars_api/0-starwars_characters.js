#!/usr/bin/node
(async () => {
  const film = await fetch(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`).then(res => res.json());
  for (const url of film.characters) console.log(await fetch(url).then(res => res.json()).then(res => res.name));
})();
