# Exércicio 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

l1 = float(input('Escolha o 1° lado! '))
l2 = float(input('Escolha o 2° lado! '))
l3 = float(input('Escolha o 3° lado! '))

equ = l1 == l2 == l3
esca = l1 != l2 != l3 != l1

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
  print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
  if equ:
    print('EQUILÁTERO!')
  elif esca:
    print('ESCALENO!')
  else:
    print('ISÓSCELES!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR um triângulo')