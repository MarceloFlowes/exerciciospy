# Exércicio 06
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite o numero das somas: '))
d = num * 2
t = num * 3
r = num ** (1/2)
print('O dobro do número escolhido é: {}'.format(d))
print('O triplo do número escolhido é: {}'.format(t))
print('A raiz do número escolhido é: {:.1f}'.format(r))