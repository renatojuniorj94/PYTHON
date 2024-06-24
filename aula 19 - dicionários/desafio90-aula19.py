"""
Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
boletim = list()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
boletim.append(aluno.copy())
print(f'Nome do aluno(a) é \033[4;34;107m{boletim[0]['nome']}\033[m')
print(f'Média é igual a {boletim[0]['media']}')
if boletim[0]['media'] < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif boletim[0]['media'] < 7:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')