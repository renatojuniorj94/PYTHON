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
    boletim = dict()
    r[] = len(n)
    r[] = max(n)
    r[] = min(n)
    for c in n:
        soma = 0
        soma += c
    media = soma / len(n)


notas()