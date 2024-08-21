"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    ok = False
    valor = 0
    try:
        while True:
            n = float(input(msg))
            if n:
                ok = True
                valor = n
            else:
                print('\033[0;31mERRO! Digite um número real válido.\033[m')
            if ok:
                break
    except (KeyboardInterrupt, ValueError):
        print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
    return valor


inteiro = leiaInt('Digite um inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')