"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A - Quantas pessoas foram cadastradas.
B - Uma listagem com as pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves.
"""

temporário = []
pessoas = []
maiorPeso = menorPeso = 0
#Quantidade de pessoas cadastradas
totPessoas = 0
while True:
    temporário.append(input('Nome: '))
    temporário.append(float(input('Peso: ')))
    #Acima, adicionamos nome e peso em uma lista temporária
    if len(pessoas) == 0:
        maiorPeso = menorPeso = temporário[1]
    else:
        if temporário[1] > maiorPeso:
            maiorPeso = temporário[1]
        if temporário[1] < menorPeso:
            menorPeso = temporário[1]
    #Abaixo adicionamos uma lista dentro de outra lista
    pessoas.append(temporário[:])
    temporário.clear()
    totPessoas += 1
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

print(f'Ao total tivemos {totPessoas} cadastradas.')
print(f'O maior peso foi {maiorPeso}, ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorPeso}, ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
print()