# Exércicio 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Qual é o preço do produto? R$'))


print('################################################')
print('####### Digite Sua Forma De Pagamento: #########')
print('################################################')
print('#### [1] à vista dinheiro/cheque ###############')
print('#### [2] à vista no cartão #####################')
print('#### [3] 2x no cartão ##########################')
print('#### [4] 3x ou mais no cartão ##################')
print('################################################')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
  total = preco - (preco * 10 / 100)
  print('O valor a ser pago é R${:.2f}'.format(total))
elif opcao == 2:
  total = preco - (preco * 5 / 100)
  print('O valor a ser pago é R${:.2f}'.format(total))
elif opcao == 3:
  total = preco
  parcela = total / 2
  print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS! '.format(parcela))
elif opcao == 4:
  total = preco + (preco * 20 / 100)
  totparc = int(input('Quantas parcelas? '))
  parcela = total / totparc
  print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS! '.format(totparc, parcela))
else:
    total = 0
    print('Opção inválida. Tente novamente.')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('################################################')
