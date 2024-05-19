"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
num.sort()
print(f'Você digitou os valores {num}')