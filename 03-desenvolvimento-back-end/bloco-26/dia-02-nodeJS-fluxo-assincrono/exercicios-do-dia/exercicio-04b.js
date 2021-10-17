const fs = require('fs').promises;

async function readSimpsons() {
  const simpsons = await fs.readFile('simpsons.json', 'utf8');
  return JSON.parse(simpsons);
}

/* async function searchSimpson(id) {
  const resultado = await readSimpsons()
  return resultado;
}

console.log(searchSimpson('1')); */

async function main(id) {
  try {
    const resultado = await readSimpsons();
    const matchSimpson = resultado.find((personagem) => personagem.id === id);
    console.log('Personagem encontrado com sucesso!!!');
    console.log(matchSimpson);
  } catch (err) {
    console.error('Personagem não encontrado');
  }
}

main('12');
//console.log(main('12'));

/* const fs = require('fs');

function readSimpsons() {
  const simpsons =fs.readFileSync('simpsons.json', 'utf8');
  return JSON.parse(simpsons);
}

function searchSimpson(id) {
  const arraySimpsons = readSimpsons();
  return arraySimpsons.find((personagem) => personagem.id === id);
  //return arraySimpsons;
}

//console.log(readSimpsons());
console.log(searchSimpson('1')); */