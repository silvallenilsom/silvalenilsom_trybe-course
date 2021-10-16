function calc(n1, n2, n3) {
  const promise = new Promise((resolve, reject) => {
    if(typeof n1 !== 'number' || typeof n2 !== 'number' || typeof n3 !== 'number')
      reject(new Error('informe apenas numeros'));

    const resultado = (n1 + n2) * n3;

    if (resultado < 50) {
      return reject(new Error('Valor muito baixo'));
    }
    resolve(resultado);

  });

  return promise;
}

  module.exports = { calc };
