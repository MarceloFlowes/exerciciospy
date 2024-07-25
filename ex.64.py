# Exércicio 64
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai para quando o usario digitar o valor 999, que é a condilçao de parada.
# No final, mostre quantos númeos foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))