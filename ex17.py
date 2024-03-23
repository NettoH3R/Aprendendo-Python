#Faça  um  Programa  para  uma  loja  de  tintas.  O  programa  deverá  pedir  o  tamanho  em  metros  quadrados  da  
# área  a  ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe a ousuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar  latas  e  galões,  de  forma  que  o  desperdício  de  tinta  seja  menor.  Acrescente  10%  de  folga  e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("digite o valor da área que vai ser pintada em m²: "))

lata_op1 = int(math.ceil((area/6)/18))
valor_op1 = lata_op1 * 80

galao_op2 = int(math.ceil((area/6)/3.6))
valor_op2 = galao_op2 * 25



print('\nNa primeira opção serão usadas {} latas, e o valor final será de {} reais\n' .format(lata_op1,valor_op1))
print('Na segunda opção serão usadas {} galões, e o valor final será de {} reais\n' .format(galao_op2,valor_op2))
