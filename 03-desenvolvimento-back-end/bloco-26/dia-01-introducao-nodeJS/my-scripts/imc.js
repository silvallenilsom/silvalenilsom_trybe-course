const calcImc = require('readline-sync');

const imc = (pe, alt) => (pe / (alt * alt)).toFixed(2);

const peso = calcImc.question('Qual seu peso? ');
const altura = calcImc.questionFloat('Qual a sua altura? ');

const resultado = imc(peso, altura);

