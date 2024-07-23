# Exércicio 31
# esenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep
v = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(v))
p = v * 0.50 if v <= 200 else v * 0.45
print('O preço a ser pago pelo serviço será de R${:.2f}'.format(p))