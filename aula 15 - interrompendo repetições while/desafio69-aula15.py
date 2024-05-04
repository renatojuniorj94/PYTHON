'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.
'''
print('=' * 30)
print(f'{'CADASTRO DE USUÁRIOS':^30}')
print('=' * 30)
maior_idade = homens = mulher_menor_idade = usuários = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        maior_idade += 1
    while idade < 0:
        print('Opção \033[1;43mINVÁLIDA!\033[m')
        idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor_idade += 1
    while sexo not in ['M', 'F']:
        print('Opção \033[1;43mINVÁLIDA!\033[m')
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    continuação = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    usuários += 1
    if continuação == 'N':
        print('—' * 30)
        break
    while continuação not in ['S', 'N']:
        print('Opção \033[1;43mINVÁLIDA!\033[m')
        continuação = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    print('—' * 30)
print('=====FIM DO PROGRAMA=====')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao total temos {homens} homens cadastrados.')
print(f'E temos {mulher_menor_idade} mulheres com menos de 20 anos.')

#Correto! :D
#Outra maneira de fazer

'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos.')'''