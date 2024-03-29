'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''

'''
https://docs.python.org/pt-br/3/library/functions.html#sum
'''

print('A seguir são os número ímpares múltiplos de 3, do 1 ao 500:\n')
for i in range(3, 501, 6):
    print(i)
soma = sum(range(3, 501, 6))
print('\nO resultado soma foi entre todos os números ímpares, que são múltiplos de 3 foi: {}'.format(soma))