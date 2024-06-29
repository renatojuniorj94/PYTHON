"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários uma lista.
No final, mostre:
A - Quantas pessoas foram cadastradas
B - A média de idade do grupo
C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média
"""
pessoa = dict()
lista = list()
todas_as_idades = mulheres = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres += 1
    while pessoa['sexo'] not in 'MmFf':
        print('Opção inválida!')
        pessoa['sexo'] = str(input('Sexo [M/F]: '))
    pessoa['idade'] = int(input('Idade: '))
    todas_as_idades += pessoa['idade']
    lista.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'Média de idade: {todas_as_idades / len(lista)}')
print(f'Total de mulheres: {mulheres}')
print(lista)