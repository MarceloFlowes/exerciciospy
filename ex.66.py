# Exércicio 66
# Crie um programa que leia vários números interos pelo teclado. O programa só pode parar quando o usuário
# digitar o valor 999, que é a condição de parada, No final, mostre quantos números foram digitados equal foi
# a soma entre eles(Desconsiderando o flag).

soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')