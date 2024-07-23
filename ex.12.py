# Exércicio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("Qual é o preço do produto? R$"))
desconto = int(input("Quanto de desconto? % "))
resultado= valor - (valor * desconto / 100)
print('Você pagando R${:.2f} tendo {}% de desconto o valor a pagar é {:.2f}'.format(valor, desconto, resultado))