'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
print('=' * 30)
print(f'{'Desafio Tabuada':^30}')
print('=' * 30)

num = int(input('Digite um número para a tabuada: '))
tab = 1
while True:
    print(f'{num} x {tab} = {num * tab}')
    tab += 1
    if tab > 10:
        break

