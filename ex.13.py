# Exércicio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual é o salario do funcionario? R$'))
rjs = float(input('Qual é o valor do reajuste? %'))
novo = sal +(sal * rjs / 100)
print('O funcionario que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(sal, rjs, novo))