#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 

g_fah = float(input('Digite a temperatura em Graus Fahrenheit: ')) 

g_cel = round(5 * ((g_fah-32) / 9),1)

print('A temperatura em graus Celsius é : {}ºC' .format(g_cel))