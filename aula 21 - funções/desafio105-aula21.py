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


'''def notas(*n, sit=False):
    """
    —> Função para analisar notas e situações de vários alunos.
    :param n: Pode receber uma quantidade indeterminada de números.
    :param sit: sit=True > Exibe situação da média de notas.
    :return: Lista com notas, total de notas, maior nota, menor nota, média e situação.
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


notas(5, 8, 7, 4.2, 3.2, 2.2, sit=True)'''

#Correto! :D
#Outra maneira de fazer...


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionario com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)