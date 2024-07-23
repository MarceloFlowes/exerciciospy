# Exércicio 49
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Escolha o numero que você deseja saber a taboada: '))
print('Você escolheu a taboada de {}'.format(n))
for c in range(0 ,11):
    print('{} x {:2} = {}'.format(n,c,n*c))