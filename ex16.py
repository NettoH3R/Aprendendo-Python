#Faça  um  programa  para  uma  loja  de  tintas.  O  programa  deverá  pedir  o  tamanho  em  metros  quadrados  da  
# área  a  ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço 
# total

import math

area = float(input("digite o valor da área que vai ser pintada em m²: "))

latas = int(math.ceil((area/3)/18))
valor = latas * 80

print('Vão ser compradas no mínimo {} latas de tintas, será um total de {} reais' .format(latas,valor))
