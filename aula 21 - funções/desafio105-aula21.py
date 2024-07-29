"""
Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação (opcional)
Adicione também as docstrings da função.
"""


def notas(*n, sit=False):
    """
    —> Função para analisar notas e situações de vários alunos.
    :param n:
    :param sit:
    :return:
    """
    itens = dict()
    itens['notas'] = n
    itens['total notas'] = len(n)
    itens['maior nota'] = max(n)
    itens['menor nota'] = min(n)
    media = sum(itens['notas']) / len(n)
    itens['media'] = media
    if sit:
        if media <= 5:
            itens['situação'] = 'Ruim'
        elif media <= 7:
            itens['situação'] = 'Razoável'
        else:
            itens['situação'] = 'Boa'
    else:
        ''

    print(itens)


notas(5, 8, 9.3, sit=True)