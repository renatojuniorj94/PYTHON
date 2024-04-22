'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

v1 = float(input('Digite o primeiro valor: '))
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
exit()

#Correto! :D

#Outra maneira de fazer:

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))