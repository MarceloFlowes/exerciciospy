# Exércicio 24
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = str(string('Em que cidade nasceu? ')).strip() #.strip = ignora os espaços
print(cid[:5].upper() == 'Santos') #.upper = joga tudo para maisculo e nao importa a forma digitada que o programa entende tudo maiusculo