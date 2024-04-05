'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''

'''
https://docs.python.org/pt-br/3/library/functions.html#sum
'''

print('A seguir são os número ímpares múltiplos de 3, do 1 ao 500:\n')
for i in range(3, 501, 6):
    print(i, end=' ')
soma = sum(range(3, 501, 6))
print('\nO resultado soma foi entre todos os números ímpares, que são múltiplos de 3 foi: {}\n'.format(soma))

#Correto! :D

#Outra maneira de fazer e ainda é melhor:

soma2 = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        # Fazendo a contagem de quantos números foram encontrados dentro da repetição.
        cont = cont + 1 # cont += 1
        soma2 = soma2 + c # soma2 += c
        print(c, end=' ')
print('\n')
print('A soma de todos os {} valores múltiplos de 3 foi: {}'.format(cont, soma2, end=' '))