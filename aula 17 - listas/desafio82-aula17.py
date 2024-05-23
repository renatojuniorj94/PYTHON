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
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print(f'Os números pares digitados foram: {par}')
print(f'Os números impares digitados foram: {impar}')
print(f'Todos os número digitados: {num}')