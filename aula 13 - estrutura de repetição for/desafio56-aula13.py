'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
'''

for c in range(1, 5):
    print('----- {}ª pessoa -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()

print('A média de idade do grupo é de {} anos.')
print('O homem mais velho tem {} anos e se chama {}.')
print('Ao todo são {} mulheres com menos de 20 anos.')