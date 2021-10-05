const calcImc = require('readline-sync');

const imc = (pe, alt) => (pe / (alt * alt)).toFixed(2);

const peso = calcImc.question('Qual seu peso? ');
const altura = calcImc.questionFloat('Qual a sua altura? ');

const resultado = imc(peso, altura);

if (resultado < 18.5) {
  console.log(`Seu IMC é ${resultado}; Resultado: Abaixo do peso (magresa)`);
} else if (resultado < 25) {
  console.log(`Seu IMC é ${resultado}; Resultado: Peso normal`);
} else if (resultado < 30) {
  console.log(`Seu IMC é ${resultado}; Resultado: Acima do peso (sobrepeso)`);
} else if (resultado < 35) {
  console.log(`Seu IMC é ${resultado}; Resultado: Obesidade grau I`);
} else if (resultado < 40) {
  console.log(`Seu IMC é ${resultado}; Resultado: Obesidade grau II`);
} else if (resultado > 40) {
  console.log(`Seu IMC é ${resultado}; Resultado: Obesidade graus III e IV`);
}