# Exércicio 73
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Vasco da Gama.

times = ('Botafogo','Flamengo','Palmeiras','Fortaleza',
         'Cruzeiro','São Paulo','Bahia','Atletico-PR',
         'Bragantino','Atletico-MG','Vasco da Gama',
         'Juventude','Internacinal','Corinthians','Criciúma',
         'Cuiabá','Grêmio','EC Vitória','Fluminense','Atlético-GO')
print('=-' * 30)
print(f' Lista de Times do Brasileiro: {times}')
print('=-' * 30)
print(f'Os 5 primeiros são {times[:5]}')
print('=-' * 30)
print(f'Os 4 ultimos são {times[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 30)
print(f'O Vasco da Gama está na {times.index('Vasco da Gama')+1} posição')