"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
"""

aluno = []
lista_final = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append([nome, nota1, nota2])
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if continuar == 'N':
            break
print(aluno)
print('-=' * 30)
print('nº   Nome        Média')
print('—' * 25)
for i, dados in enumerate(aluno):
    print(f'{i: <5}{dados[0]: <12}{(dados[1] + dados[2]) / 2:.2f}')
print('—' * 25)
while True:
    notas = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))
    #Resolver o laço de repetição abaixo:
    '''while notas not in aluno[notas]:
        print('O aluno não consta na lista. Tente novamente!')
        notas = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))'''
    if notas == 999:
        break
    print(f'As notas de {aluno[notas][0]} são [{aluno[notas][1]}, {aluno[notas][2]}]')

#Correto! :D
#Outra maneira de fazer...

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota01 = float(input('Nota 1: '))
    nota02 = float(input('Nota 2: '))
    media = (nota01 + nota02) / 2
    ficha.append([nome, [nota01, nota02], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":8.}')
print('—' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('—' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')