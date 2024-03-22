#João  Papo-de-Pescador,  homem  de  bem,  comprou  um  microcomputador  para  controlar  o  
# rendimento  diário  de  seu trabalho. Toda vez que ele traz um peso de peixes maior que o 
# estabelecido pelo regulamento de pescado estado de São Paulo (50 quilos) deve pagar uma multa
#  de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia  a  variável 
# peso (peso  de  peixes)  e  calcule  o  excesso.  Gravar  na  variável excesso a  quantidade  de  quilos  
# além  do limite  e na  variável multa o valor  da  multa  que  João deverá  pagar. Imprima  os  dados do
#  programa com  as mensagens adequadas.

kg = float(input('Digite o peso da quantidade de peixes pecados em Kg: '))

if kg > 50:
    kg = kg - 50
    multa = kg * 4
    print('O excesso foi de {}Kg, portanto a multa será de: R${}' .format(kg,multa))
else:
    print('A quantidade pescada está dentro do regulamento de pescado estado de São Paulo')
