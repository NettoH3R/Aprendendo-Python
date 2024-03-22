# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a.o produto do dobro do primeiro com metade do segundo.
# b.a soma do triplo do primeiro com o terceiro.
# c.o terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número Real(decimal): '))

a = (n1 * 2) * (n2 / 2)
b = (3 * n1) + n3
c = n3**3

print("a) O produto do dobro do primeiro número com metade do segundo número é: {}" .format(a))
print("b) A soma do triplo do primeiro número com o terceiro número é: {}" .format(b))
print("c) o terceiro número elevado ao cubo é: {}" .format(c))