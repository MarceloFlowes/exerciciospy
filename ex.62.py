# Exércicio 62
# Melhore o DESAFIO 61, perguntando para o usuario s ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('=-=' * 10)
t = int(input("Digite o Primeiro termo: "))
r = int(input("Digite a Razão da PA: "))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end=' ')
        termo += r
        cont += 1
    print('PAUSA !')
    mais = int(input('Quantos termoos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))