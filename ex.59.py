# Exércicio 59
# Crie um programa que leia dois valores e moster um menu na tela:
# (1) Somar
# (2) Multiplicar
# (3) Maior
# (4) Novos Números
# (5) Sair Do Programa
# Seu programa deverá realizar a operação solicitada em cada casa
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair Do Programa''')
    opcao = int(input('>>>>>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A Multiplicação de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if  n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente')
    print('=-=' * 10)
    sleep(3)
print('Fim do programa! Volte sempre!')
