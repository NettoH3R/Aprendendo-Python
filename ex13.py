# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
# asseguintes fórmulas:
# a.Para homens: (72.7*h) -58
# b.Para mulheres: (62.1*h) -44.7

altura = float(input('Digite a altura em metros: '))
peso_h = round((72.7 * altura) - 58 ,1)
peso_m = round((62.1 * altura) - 44.7 ,1)

print('\n Baseado na altura digitada {}m \nO peso ideal para homens seria: {}Kg \n' .format(altura,peso_h))
print('Baseado na altura digitada {}m \nO peso ideal para mulheres seria: {}Kg' .format(altura,peso_m))