# Exércicio 39
# Faça u programa que leia o ano de nascimento de um jovem e finforme, de acordo com sua idade, se ele (ainda vai se alistar) ao serviço militar,
# se é a (hora de se alistar) ou sejá (passou do tempo) do alistamento. Seu programa também deverá mostrar o tempo que falta ou que
# passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
  print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
  saldo = 18 - idade
  print('Ainda faltam {} anos para o alistamento.'.format(saldo))
  ano = atual + saldo
  print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
  saldo = idade - 18
  print('Você deveria ter se alistado há {} anos.'.format(saldo))
  ano = atual - saldo
  print('Seu alistamento foi em {}'.format(ano))