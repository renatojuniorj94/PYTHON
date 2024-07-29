"""
Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa
se encerrará.
OBS: Use cores.
"""


def ajuda():
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


ajuda()