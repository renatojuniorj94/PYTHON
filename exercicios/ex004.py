#Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

text = input('Digite algo: ')
print(type(text))
print('isnumeric? {}'.format(text.isnumeric()))
print('isalnum? {}'.format(text.isalnum()))
print('isspace? {}'.format(text.isspace()))