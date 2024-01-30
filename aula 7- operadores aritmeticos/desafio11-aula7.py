#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule sua área e a quantidade de tinta necessária
#para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\n'
      'Você vai precisar de {} litros de tinta.'.format(a, l, a*l, (a*l) / 2))

#Correto! :D
