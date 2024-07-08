"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários uma lista.
No final, mostre:
A - Quantas pessoas foram cadastradas
B - A média de idade do grupo
C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média
"""
"""pessoa = dict()
lista = list()
todas_as_idades = mulheres = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres += 1
    while pessoa['sexo'] not in 'MmFf':
        print('Opção inválida!')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] == 'F':
            mulheres += 1
    pessoa['idade'] = int(input('Idade: '))
    todas_as_idades += pessoa['idade']
    lista.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
media = todas_as_idades / len(lista)
print('-=' * 40)
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'Média de idade: {media}')
print(f'Total de mulheres: {mulheres}')
print('Pessoas com idade acima da média:')
for p in lista:
    if p['idade'] >= media:
        print(f'Nome: {p['nome']}, Idade: {p['idade']}')"""

#Correto! :D
#Outra maneira de fazer...

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media} anos.')
print('As mulheres cadastradas foram:')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}')
print('Lista das pessoas acima da média:')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')