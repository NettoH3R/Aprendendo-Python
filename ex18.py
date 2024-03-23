#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule   e   informe   o   tempo   aproximado   de   download   do   arquivo   usando   este   link   (em   minutos).

arquivo = float(input('Digite o peso do arquivo em MB: '))
internet = float(input('Digite a velocidade da sua interner em Mbps: '))

velocidade = arquivo/internet

velocidade = round(velocidade/60,1)
print('O arquivo demorará {} minutos para baixar' . format(velocidade))
