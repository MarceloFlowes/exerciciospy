# Exércicio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto '))
ca = float(input('Compirmento do cateto adjacente '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#co = float(input('Comprimento do cateto oposto '))
#ca = float(input('Compirmento do cateto adjacente '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))'''