# Exércicio 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('Analisando um Triangulo')
print('-=-' * 20)
p = float(input('Digite o primeiro ângulo: '))
s = float(input('Digite o segundo ângulo: '))
t = float(input('Digite o terceiro ângulo: '))
if p < (s + t) and s < (p + t) and t < (p + s):
  print('Analisando os ângulos pode sim se forma um Triângulo')
else:
  print('Analisando os ângulos NÂO pode se formar um Triângulo')