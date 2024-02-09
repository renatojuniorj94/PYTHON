'''Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas
-O nome com todas minúsculas
-Quantas letras ao todo ( sem considerar espaços).
-Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
split = nome.split()
qtd_letras = len(split)
n1 = len(split[0])
print('{}\n'
      '{}\n'
      'Seu nome possui {} letras.\n'
      'E o primeiro nome é {} e tem {} letras'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), split[0], n1))

#Correto! :D

#Outra maneira

print('E o primeiro nome é {} e tem {} letras'.format(split[0], nome.find(' ')))
