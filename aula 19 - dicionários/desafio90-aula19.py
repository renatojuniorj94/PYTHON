"""
Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
boletim = list()
for c in range(1):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input('Média: '))
boletim.append(aluno.copy())
for a in aluno.items():
    print(f'Nome do aluno(a) é igual a {a}')
    print(f'Média é igual a {m}')
'''if m < 5:
    print('REPROVADO!')
else:
    print('APROVADO!')'''
print(boletim)