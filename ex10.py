#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

g_cel = float(input('Digite a temperatura em Graus Celsius: ')) 


g_fah = round((g_cel * 9/5) + 32 ,1)

print('A temperatura em graus Fahrenheit é : {}ºF' .format(g_fah))