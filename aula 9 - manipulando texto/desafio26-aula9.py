'''
Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A"
-Em que posição ela aparece a primeira vez.
-Em que posição ela aparece a última vez.
'''
nome = str(input('Digite seu nome: ')).strip()
print('Em seu nome aparece {} vezes a letra "a"'.format(nome.upper().count('A'[0:])))
print('Ela aparece pela primeira vez na posição {}'.format(nome.lower().find('a') + 1))
print('E aparece pela última vez na posição {}'.format(nome.upper().rfind('A') + 1))

#Correto! :D
