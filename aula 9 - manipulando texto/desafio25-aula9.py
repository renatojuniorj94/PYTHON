'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
nome = str(input('digite seu nome completo: ')).strip()
nome_m = nome.upper()
print('{}, possui "Silva" no nome? {}'.format(nome, 'SILVA' in nome.upper()))

#Correto! :D