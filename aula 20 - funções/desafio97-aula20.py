"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, mundo!')
Saída:
~~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~~
"""


def escreva(msg):
    for c in msg:  # Não há necessidade em usar for nesse programa.
        ler = len(msg)
    print('~' * ler)
    print(msg)
    print('~' * ler)


escreva('  Copa Libertadores  ')
escreva('  Brasileirão  ')
escreva('  Copa do Brasil  ')
escreva('  CLUBE DE REGATAS DO FLAMENGO  ')
escreva('  CURSO DE PYTHON NO YOUTUBE (CURSO EM VÍDEO)  ')

#Correto! :D
#Outra maneira de fazer...


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')