'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''

'''
https://docs.python.org/pt-br/3/library/functions.html#sum
'''

for i in range(3, 501, 6):
    '''print(i)'''
    print(sum(range(3, 501, 6)))