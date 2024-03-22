#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
#  total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
# para o sindicato, faça um programa que nos dê:
# a.salário bruto.
# b.quanto pagou ao INSS.
# c.quanto pagou ao sindicato.
# d.o salário líquido.
# e.calcule os descontos e o salário líquido, conforme a tabela abaixo:

valor_hr = float(input('Quanto você ganha por hora? \n'))
horas_tb = float(input('Quantas horas você trabalha por mês? \n'))

salario_bruto = valor_hr * horas_tb

salario_liquido = round(salario_bruto * 0.89,2)
inss = round(salario_bruto * 0.11,2)

imp_renda = round(salario_liquido * 0.08,2)
salario_liquido = round(salario_liquido * 0.92,2)

sindicato = round(salario_liquido * 0.05,2)
salario_liquido = round(salario_liquido * 0.95,2)

print('-Salário bruto: R${}\n-INSS: R${}\n-Imposto de Renda: R${}\n-Sindicato: R${}\n-Salário líquido: R${}\n' .format(salario_bruto,inss,imp_renda,sindicato,salario_liquido))


