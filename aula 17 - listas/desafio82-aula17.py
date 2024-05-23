"""
Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, crie duas listas que vão conter apenas os valores pares e
os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

num = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    num += num
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    print('par', par)
    print('impar', impar)
    print(num)
    '''continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'S' or 'N':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ')
    if continuar == 'N':
        break'''