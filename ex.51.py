# Exércicio 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t = int(input("Digite o termo: "))
r = int(input("Digite a razão: "))
d = t + (10-1) * r
for c in range(t ,d + r,r):
    print('{}'.format(c), end=' → ')
print('THE END!')
