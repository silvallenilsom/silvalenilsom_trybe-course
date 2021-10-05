const speedParams = require('readline-sync');

const veloMedia = (dist, temp) => dist / temp;

const distancia = speedParams.questionInt('Qual a distância percorrida(metros)?');
const tempo = speedParams.questionInt('Qual o tempo de duração(segundos)?');

const resultado = veloMedia(distancia, tempo);

console.log(`resultado: ${resultado} Mts/segundo`);