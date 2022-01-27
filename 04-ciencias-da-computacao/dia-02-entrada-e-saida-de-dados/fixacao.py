import csv

# Exercício 1: Faça um programa que solicite o nome de uma pessoa usuária e
# imprima-o na vertical.
""" nome = input("Digite seu nome:\n")
for letra in nome:
    print(letra) """

# Exercício 2: Escreva um programa que receba vários números naturais e calcule
# a soma desses valores. Caso algum valor da entrada seja inválido, por exemplo
# uma letra, uma mensagem deve ser exibida, na saída de erros, no seguinte
# formato: "Erro ao somar valores, {valor} é um valor inválido". Ao final, você
# deve imprimir a soma dos valores válidos.
""" numbers = input("digite varios numeros separados por espaço:\n")
numbers_list = numbers.split(" ")
print(numbers_list)
sum = 0
for num in numbers_list:
    if not num.isdigit():
        print(f"{num} não é um numero, não será somado")
    else:
        sum += int(num)

print(f"A soma dos valores validos é {sum}") """

# Manipulando a leitura e escrita em um arquivo

# Abrindo um arquivo. Ele será reconhecido no sistema como 'arquivo' e ao
# termino da manipulação ele deverá ser fechado e receberá o nome passado na
# função open e salvo, caso não seja especificado, no local onde está sendo
# executada a função.
""" arquivo = open("texto-de-exemplo.txt", mode="w")

arquivo.write("MEUS PERSONAGENS FAVORITOS\n")
arquivo.write("Deku\n")
arquivo.write("Bakugo\n")
arquivo.write("Todoroki\n")
arquivo.write("Roy Mustang\n")

# Após a escrita concluida utiliza-se close para encerrar o processo de escrita
arquivo.close()

# Para ler o arquivo utiliza-se a função read
arquivo = open("texto-de-exemplo.txt")
conteudo = arquivo.read()
print(conteudo)
arquivo.close() """

a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = [
    1,
    2,
    3,
]  # Quando um * está presente no desempacotamento, os valores são
# desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]
