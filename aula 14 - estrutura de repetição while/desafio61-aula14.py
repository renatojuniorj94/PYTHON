'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando o 10 primeiros termos da progressão usando a estrutura while.
'''
print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
pa = termo
cont = 1

while cont <= 10:
    print('{} > '.format(pa), end='')
    pa += razão
    cont += 1
print('FIM')

#Correto! :D