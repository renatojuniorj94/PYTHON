"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A - Quantos números foram digitados.
B - A lista de valores, ordenada de forma decrescente.
C - Se o valor 5 foi digitado e está ou não na lista
"""

valores = list()
contador = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    contador += 1
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O número 5 não está na lista')
print(f'Foram digitados {contador} números.')
valores.sort(reverse=True)
print(valores)