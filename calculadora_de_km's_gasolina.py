 # Exércicio Pessoal (Queria calcular quato vou receber)
# Combustível
# Fazer isso é relativamente simples: basta pesquisar a média de consumo do carro e o valor médio do combustível.
# Com esses dados em mãos, divida o preço pelo consumo. Se o valor do combustível é de R$ 5,00 por litro e o consumo é 10 km/L,
# a conta fica: 5,00 / 10 = 0,5. Ou seja, cada quilômetro custa R$ 0,5.

rodado = float(input('Quantos kms você percorreu? '))
valorgas = float(input('Qual é o valor do seu combustível? R$'))
consumo = float(input('Qual é o consumo do sua MOTO em Km/l? '))

quantidade = rodado / consumo
total = quantidade * valorgas
print('O valor a ser pago é R${:.2f}'.format(total))