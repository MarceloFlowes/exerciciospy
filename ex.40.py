# Exéricio 40
# Crie um programa que leia duas notas de um aluno e calcule sua media, motrando uma mensagem no final, de acordo com a média atingida:
#-Média abaido de 5.0: REPROVAÇÃO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior : APROVAÇÃO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media <= 5.0:
  print('Você está REPROVADO! Sua média: {}'.format(media))
elif media <= 6.9:
  print('Você está de RECUPERAÇÃO! Sua média: {}'.format(media))
elif media >= 7.0:
  print('Você está APROVADO! Sua média {}'.format(media))