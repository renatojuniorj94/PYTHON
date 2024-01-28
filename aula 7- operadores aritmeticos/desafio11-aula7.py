#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule sua área e a quantidade de tinta necessária
#para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
print('Você vai precisar de {:.0f} litros de tinta.'.format((a*l) / 2))
