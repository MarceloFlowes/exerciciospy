# Exércicio 04
# Crie um programa que saiba dissecar uma variavel.

a = input('Digite uma frase: ')
print('O tipo primitivo deste valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É Alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())