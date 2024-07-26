# Exércicio 69

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
tot18 = tothomen = totmulher20 = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual Sexo? [M/F] ')).strip().upper()[0]
    idade = int(input('Qual sua idade? '))
    if idade < 18:
        tot18 += 1
    if sexo == 'M':
        tothomen += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'A o todo temos {tothomen} homens cadastrados.')
print(f'E temos {totmulher20} mulheres com menos de 20 anos.')

