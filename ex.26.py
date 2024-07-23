# Exércicio 26
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A'))) # .count conta quantas vezes a letra A aparece na frase
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #.find mosta a primeira posição da leta A (+1* pois começa a contar no 0 +1 faz ficar mais organizado)
print('A a ultima letra A apareceu na posição {}'.format(frase.rfind('A')))