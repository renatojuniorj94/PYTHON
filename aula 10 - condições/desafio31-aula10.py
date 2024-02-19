'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até
200Km e R$ 0,45 para viagens mais longas.
'''
km = float(input('Digite quantos Kms vai ter sua viagem: '))
if km <= 200:
    print('O valor da passagem é de R$ {:.2f}'.format(km * 0.50))
else:
    print('O valor da passagem é de R$ {:.2f}'.format(km * 0.45))

#Cooreto! :D

#Outra maneira de fazer...
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))

#Usando if inline ou operador ternário:
'''
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))
'''