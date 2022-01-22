a = 10
b = 5

# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e
# b = 5. Mostre o resultado das 7 operações básicas (soma, subtração,
# ultiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo
# essas variáveis.
print('\nexercicio 01')
print("a =", a, "b =", b)
print("adição:", a + b)
print("subtração:", a - b)
print("multiplicação:", a * b)
print("divisão:", a / b)
print("potenciação:", a ** b)
print("quociente:", a // b)
print("resto:", a % b)

# Exercício 2: Declare e inicialize uma variável: hours = 6 . Quantos minutos
# têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e
# seconds que recebem os respectivos resultados das contas. Depois, imprima
# cada uma delas.
print('\nexercicio 02')
hours = 6
minutes = hours * 60
seconds = minutes * 60
print(minutes)
print(seconds)

# Exercício 4: Suponha que o preço de capa de um livro seja 24,20, mas as
# livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro
# exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de
# atacado para 60 cópias? Escreva uma expressão que receba o custo total e
# a imprima.
print('\nexercicio 04')
livro = 24.20
desconto = 0.4
qtd_unidades = 60
livro_c_desconto = (1 - desconto) * livro
vlr_frete = ((qtd_unidades - 1) * 0.75) + 3
total_pedido = livro_c_desconto * qtd_unidades + vlr_frete
print(total_pedido)

# Lista para exercicios 5 e 6
trybe_course = ["Introdução", "Front-end", "Back-end"]

# Exercício 5: Adicione o elemento "Ciência da Computação" à lista.
trybe_course.append('Ciência da Computação')

# Exercício 6: Acesse e altere o primeiro elemento da lista para "Fundamentos".
print('\nexercicio 06')
trybe_course[0] = 'Fundamentos'
print(trybe_course[0])

# Exercício 7: Um conjunto ou set pode ser inicializado utilizando-se também o
# método set() . Inicialize uma variável com essa função var = set() e adicione
# seu nome ao conjunto utilizando um dos métodos vistos acima. Depois, imprima
# a variável e confira se o retorno é: {'seu_nome'}.
print('\nexercicio 07')
var = set()
var.add('lenilsom')
print(var)

# Dicioinario para exercicios 8 a 10
info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

# Exercício 8: O que acontecerá se você tentar acessar o valor da
# chave "personagem" como fazíamos em JavaScript, utilizando object.key ?

# Exercício 9: Insira no objeto uma nova propriedade com o nome de
# chave "recorrente" e o valor "Sim". Em seguida, imprima o objeto no console.
info['recorrente'] = 'sim'

# Exercício 10: Remova a propriedade cuja chave é "origem" e imprima o objeto
# no console.
print('\nexercicio 10')
del info["origem"]
print(info)

# Exercício 13: O Fatorial de um número inteiro é representado pela
# multiplicação de todos os números predecessores maiores que 0. Por exemplo o
# fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5 . Escreva um código que
# calcule o fatorial de um número inteiro.
print('\nexercicio 13')
num_fatorial = 5
resultado_fatorial = 1

for index in range(1, (num_fatorial + 1)):
    resultado_fatorial = resultado_fatorial * index

print('resultado', resultado_fatorial)


# Exercício 14: Um sistema de avaliações registra valores de 0 a 10 para cada
# avaliação. Após algumas mudanças estes valores precisam ser ajustados para
# avaliações de 0 a 100. Dado uma sequência de avaliações
# ratings = [6, 8, 5, 9, 10] . Escreva um código capaz de gerar as avaliações
# após a mudança. Neste caso o resultado deveria ser [60, 80, 50, 90, 100] .
ratings = [6, 8, 5, 9, 10]
new_ratings = []
for rating in ratings:
    new_ratings.append(rating * 10)
print('\nexercicio 14')
print(new_ratings)
# Experimente utilizar a sintaxe de compreensão de listas.

# Exercício 15: Percorra a lista do exercício 14 e imprima "Múltiplo de 3" se o
# elemento for divisível por 3.

for rating in new_ratings:
    if rating % 3 == 0:
        print(rating, 'É multiplo de 3')
