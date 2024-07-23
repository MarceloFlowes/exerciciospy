# Exércicio 37
# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:
# 1 para Binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão: )
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
  print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
  print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
  print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
elif opcao >= 4:
  print('Opção inválida. Tente novamente.')
else :
  print('Opção inválida. Tente novamente.')
