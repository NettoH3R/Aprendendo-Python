#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hr = float(input('Quanto você ganha por hora? \n'))
horas_tb = float(input('Quantas horas você trabalha por mês? \n'))

salario = valor_hr * horas_tb

print('Seu salário mensal é de: R${}' .format(salario))