const fs = require('fs').promises;

async function functionSimpsons() {
  const arquivo = await fs.readFile('simpsons.json', 'utf8')
  return JSON.parse(arquivo);
}

functionSimpsons()
  .then((simpsons) => {
    const personagens = simpsons.map(({ id, name }) => `${id} - ${name}`);
    console.log(personagens);
  });