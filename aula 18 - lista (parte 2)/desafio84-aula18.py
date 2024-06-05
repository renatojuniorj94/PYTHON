'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A - Quantas pessoas foram cadastradas.
B - Uma listagem com as pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves.
'''

pessoas = []
maisPeso = []
menosPeso = []
totPessoas = 0
while True:
    nome = str(input('Nome: '))
    pessoas.append(nome)
    peso = float(input('Peso: '))
    pessoas.append(peso)
    totPessoas += 1
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

print(pessoas)
print(f'Ao total tivemos {totPessoas} cadastradas.')
