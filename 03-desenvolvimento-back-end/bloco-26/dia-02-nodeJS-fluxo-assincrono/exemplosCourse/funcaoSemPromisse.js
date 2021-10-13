function calcularDivisao(num1, num2) {
  if (num2 == 0) throw new Error('Não pode ser feita divisão por zero');

  const resultado = num1 / num2;

  return resultado;
}

try {
  const resultado = calcularDivisao(2, 1);
  console.log(`Resultado: %s`, resultado);
} catch (error) {
  console.log("Erro: %s", error.message);
}
