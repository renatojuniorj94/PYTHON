'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

'''v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
o = int(input('Você deseja:\n'
    '[1] Somar\n'
    '[2] Multiplicar\n'
    '[3] Maior\n'
    '[4] Novos números\n'
    '[5] Sair do programa\n>>> '))

while o != 5:
    if o == 1:
        print('{:.0f}'.format(v1 + v2))
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        o = int(input('Você deseja:\n'
                      '[1] Somar\n'
                      '[2] Multiplicar\n'
                      '[3] Maior\n'
                      '[4] Novos números\n'
                      '[5] Sair do programa\n>>> '))
    if o == 2:
        print('{:.0f}'.format(v1 * v2))
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        o = int(input('Você deseja:\n'
                      '[1] Somar\n'
                      '[2] Multiplicar\n'
                      '[3] Maior\n'
                      '[4] Novos números\n'
                      '[5] Sair do programa\n>>> '))
    if o == 3:
        if v1 > v2:
            print(v1, " é o maior.")
        elif v1 < v2:
            print(v2, ' é o maior')
        else:
            print('Os números são iguais')
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        o = int(input('Você deseja:\n'
                      '[1] Somar\n'
                      '[2] Multiplicar\n'
                      '[3] Maior\n'
                      '[4] Novos números\n'
                      '[5] Sair do programa\n>>> '))
    if o == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        o = int(input('Você deseja:\n'
                      '[1] Somar\n'
                      '[2] Multiplicar\n'
                      '[3] Maior\n'
                      '[4] Novos números\n'
                      '[5] Sair do programa\n>>> '))
print('Obrigado por usar nosso sistema, até breve!')
exit()'''

#Correto! :D

#Outra maneira de fazer:

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0

while opção != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMERO
[5] SAIR DO PROGRAMA''')
    opção = int(input('Digite sua opção >>> '))
    if opção == 1:
        print('\033[1;31m{}\033[m'.format(n1 + n2))
        print('=*' * 10, end='')
        print('=')
    elif opção == 2:
        print('\033[1;31m{}\033[m'.format(n1 * n2))
        print('=*' * 10, end='')
        print('=')
    elif opção == 3:
        if n1 > n2:
            print('\033[1;31m{}\033[m'.format(n1))
            print('=*' * 10, end='')
            print('=')
        else:
            print('\033[1;31m{}\033[m'.format(n2))
            print('=*' * 10, end='')
            print('=')
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('=*' * 10, end='')
        print('=')
    elif opção == 5:
        print('\033[1;32mObrigado por usar nosso sistema!\033[m')
    else:
        print('\033[31mOpção inválida!\033[m Tente novamente...')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('=*' * 10, end='')
        print('=')