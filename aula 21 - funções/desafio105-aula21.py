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
    boletim = list()
    itens = dict()
    itens['total de notas'] = n
    itens['número de notas'] = len(n)
    itens['maior nota'] = max(n)
    itens['menor nota'] = min(n)
    soma = 0
    boletim.append(itens['total de notas'])
    """for c in boletim:
        soma += c
    media = soma / len(itens['total de notas'])"""
    print(boletim)


notas(5, 8)