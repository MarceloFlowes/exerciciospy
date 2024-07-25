# Exércicio 61
# Refaça o DESAFIO 51, lendo o primeiro trmo e arazão de uma PA
# Mostrando os 10 primeiros termos da progressão usando a estrutura while
print('Gerador de PA')
print('=-=' * 10)
t = int(input("Digite o termo: "))
r = int(input("Digite a razão: "))
termo = t
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end=' ')
    termo += r
    cont += 1
print('THE END!')