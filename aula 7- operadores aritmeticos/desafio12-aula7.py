#Faça um algoritmo que leia o preço de un produto e mostre
# seu novo preço, com 5% de desconto.

v = float(input('Digite o valor do produto: R$ '))
print('O valor final do produto com 5% de desconto irá custar R$ {:.2f}'.format((v/100)*95))