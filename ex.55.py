# Exércicio 55
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pess in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if pess < menor:
            menor = peso
print('O MAIOR peso lido foi de {}Kg'.format(maior))
print('O MENOR peso lido foi de {}Kg'.format(menor))

