'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
'''

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_velho = 0
mulher_20 = 0

for c in range(1, 5):
    print('----- {}ª pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if sexo not in ['M', 'm', 'f', 'F']:
        print('\033[31mSexo inválido!\033[m')
        exit()

    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_20 += 1
media_idade = soma_idade / 4

print('A média de idade do grupo é de {:.0f} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_20))
