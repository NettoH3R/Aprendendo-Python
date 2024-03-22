#Tendo comodados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,usando 
# a seguinte fórmula: (72.7*altura) -58

altura = float(input('Digite sua altura em metros: '))
peso = round((72.7 * altura) - 58 ,1)

print('Baseado sua altura {}m seu seu peso ideal seria: {}Kg' .format(altura,peso))