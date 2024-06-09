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