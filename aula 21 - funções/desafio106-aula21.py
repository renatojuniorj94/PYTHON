"""
Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa
se encerrará.
OBS: Use cores.
"""


"""def ajuda():
    while True:
        from time import sleep
        msg_1 = 'SISTEMA DE AJUDA PyHELP'
        print('\033[1;42m~' * len(msg_1))
        print(msg_1)
        print('~' * len(msg_1))
        resp = str(input('\033[mFunção ou biblioteca > ')).lower()
        if resp == 'fim':
            fim = 'ATÉ LOGO!'
            print('\033[1;41m~' * len(fim))
            print(fim)
            print('~' * len(fim))
            break
        msg_2 = f"Acessando o manual do comando '{resp}'"
        print('\033[1;44m~' * len(msg_2))
        print(msg_2)
        print('~' * len(msg_2))
        sleep(1)
        print('\033[1;30;107m')
        help(resp)


ajuda()"""

#Correto! :D
#Outra maneira de fazer...

from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;97m'      # 6 - branco
     )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)