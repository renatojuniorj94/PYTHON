'''
Crie um programa que mostre na tela todos os números pares
que estão no intervalo entre 1 e 50
'''

for c in range(2, 51, 2):
    print(c, end=' ')
print('\n')

#Correto! :D

#Outra maneira de fazer: (Acima é melhor porque economiza repetições e consequentemente memória)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)