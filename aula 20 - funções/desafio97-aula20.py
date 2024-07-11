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
#ler = len(escreva)


def escreva(msg):
    for c in msg:
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
