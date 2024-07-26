# Exércicio 67
# Faça um programa que mostre a taboada de varios numeros, um de cada vez, para cada valor digitado
# pelo usuario. O programa será interrompido quando o número solicitado for negativo.

cont = 0
while True:
    n = int(input('Qual número você deseja saber a taboada? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Progama Encerrado!')
