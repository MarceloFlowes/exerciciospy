# Exércicio 38
#Escreva um  progrma ue leia dois números inteiros e compre-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não exite valor maior, e os dois são igual
print('Para compara qual numero é maior informe o valor!')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
  print('O numero {} é  maior que o {}'.format(num1, num2))
elif num2 > num1:
  print('O numero {} é maior que o {}'.format(num2, num1))
else:
  print('Não existe valor maior, os dois são iguais')