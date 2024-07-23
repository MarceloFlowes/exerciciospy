# Exércicio 36
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Quanto custa a casa? R$'))
salario = float(input('Quanto você recebe? R$'))
anos = int(input('Quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('O valor cobrado para o imovel, que está avaliado em R${:.2f} em {} anos '.format(casa, anos), end='')
print(' nosso serviço será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
     print('Empréstimo poder ser CONCEDIDO!')
else:
     print('Empréstimo NEGADO!')