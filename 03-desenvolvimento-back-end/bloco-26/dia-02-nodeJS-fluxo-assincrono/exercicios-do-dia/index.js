const calculo = require('./calcNumbers')

const randomNumber = () => Math.floor(Math.random() * 100 + 1);

n1 = randomNumber();
n2 = randomNumber();
n3 = randomNumber();

calculo.calc(n1, n2, n3)
  .then((result) => console.log(`Resultado: ${result}`))
  .catch((e) => console.log(`Erro: ${e.message}`));