'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$ 1000.
C - Qual é o nome do produto mais barato.
'''

total = mil = valor_barato = cont = 0
nome_barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: \033[32mR$\033[m '))
    total += preço
    cont += 1
    # Simplificando o bloco abaixo
    if cont == 1 or preço < valor_barato:
        valor_barato = preço
        nome_barato = produto
    '''if cont == 1:
        mais_barato = preço
        barato = produto
    else:
        if preço < mais_barato:
            mais_barato = preço
            barato = produto'''
    if preço >= 1000:
        mil += 1
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
    while continua not in ['S', 'N']:
        print('Opção \033[1;43mINVÁLIDA!\033[m')
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('—' * 30)
print('—' * 10 + 'FIM DO PROGRAMA' + '—' * 10)
print(f'O total da compra foi R$ {total}')
print(f'Temos {mil} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R$ {mais_barato}')

#Correto! :D