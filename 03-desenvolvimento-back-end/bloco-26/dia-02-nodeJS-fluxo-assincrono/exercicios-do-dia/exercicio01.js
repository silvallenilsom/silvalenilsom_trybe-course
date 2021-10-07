function calculate(n1, n2, n3) {
  return new Promise((resolve, reject) => {
    if (typeof n1 !== 'number' || n2 !== 'number' || n3 !== 'number') {
      reject('informe apenas numeros');
    }

    const resultado = ((n1 + n2) * n3);
    if (resultado < 50) {
      reject('Valor inferior a 50');
    }

    resolve(resultado);

  });
}

calculate(2, 3, 4);
