"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais:
O nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s).')


n = str(input('Nome do jogador: '))
g = str(input(f'Quantos gols {n} marcou? '))
if g.isnumeric():  # Se 'g' receber um dado numérico: 'g' vira int()
    g = int(g)
else:  # Se não receber um dado como string, ele recebe '0' como padrão.
    g = 0
if n.strip() == '':  # Se 'n' receber um dado em branco, a função ficha vai receber 'g' em 'gols' e
    #'nome' recebe a resposta padrão ('<desconhecido>')
    ficha(gols=g)
else:
    ficha(n, g)

#Desafio feito na aula de resolução.