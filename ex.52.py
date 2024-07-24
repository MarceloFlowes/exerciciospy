# Exércicio 52
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite o número que você deseja saber se é primo: '))
t = 0 #total
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033 O numero {} foi divisível {} vezes'.format(n,t))
if t == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso eles NÂO É PRIMO!')