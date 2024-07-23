# Exércicio 08
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite o valor em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('A medida de {}m corresponde a {:.2f}mm, {:.2f}cm, {:.2f}dm,'.format(m, mm, cm, dm))
print('{:.2f}dam, {:.2f}hm e {:.2f}km'.format(dam, hm, km))