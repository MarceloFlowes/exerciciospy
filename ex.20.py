# Exércicio 20
# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Primeira Pessoa: '))
n2 = str(input('Segunda Pessoa: '))
n3 = str(input('Terceira Pessoa: '))
n4 = str(input('Quarta Pessoa: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)