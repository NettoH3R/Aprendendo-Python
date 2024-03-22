# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o valor de um dos lados do quadrado: '))

area = lado * lado

print("A área do quadrado informado é de: {}" .format(area))

area = area * 2

print('O dobro dessa área é de: {}' .format(area))