'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

maior_idade = 0
menor_idade = 0
from datetime import date
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - pessoa
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior_idade))

if menor_idade > 0:
    print('E também tivemos {} pessoas menores de idade.'.format(menor_idade))
else:
    print('Na lista não consta nenhum menor de idade.')

#Correto! :D