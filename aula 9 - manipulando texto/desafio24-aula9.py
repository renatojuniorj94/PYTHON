'''
Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO".
'''
city = str(input('Digite o nome da sua cidade: '))
city_m = city.upper().split()
print('Sua cidade começa com o nome "Santo"? {}'.format('SANTO' in city_m[0]))

#Correto! :D

#Outra maneira:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
