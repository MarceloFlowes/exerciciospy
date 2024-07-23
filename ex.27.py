# Exércicio 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split() #Split fatia a string(separa a string em lista)
print('Muito prazer em conhece-lo {}'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))#len serve para vê a string em listas