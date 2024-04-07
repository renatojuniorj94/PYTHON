'''
Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razão #Ou (10)
for c in range(termo, decimo + razão, razão):
    print('{}'.format(c), end=' ➝ ')
print('FIM')