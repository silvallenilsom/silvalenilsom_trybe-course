a = 10
b = 5

# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo essas variáveis.
print("a =", a, "b =", b)
print("adição:", a + b)
print("subtração:", a - b)
print("multiplicação:", a * b)
print("divisão:", a / b)
print("potenciação:", a ** b)
print("quociente:", a // b)
print("resto:", a % b)

# Exercício 2: Declare e inicialize uma variável: hours = 6 . Quantos minutos têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos resultados das contas. Depois, imprima cada uma delas.
hours = 6
minutes = hours * 60
seconds = minutes * 60
print(minutes)
print(seconds)

# Exercício 4: Suponha que o preço de capa de um livro seja 24,20, mas as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que receba o custo total e a imprima.

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
trybe_course[0] = 'Fundamentos'
print(trybe_course[0])
