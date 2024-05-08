'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A - Quantos vezes apareceu o valor 9.
B - Em que posição foi digitado o primeiro valor 3.
C - Quais foram os números pares.
'''

cont = 0
tupla = par = ()
for c in range(1, 5):
    num = int(input('Digite um número: '))
    tupla += num,
    if num == 9:
        cont += 1

    if num % 2 == 0:
        par += num,

print(f'Você digitou os números {tupla}')
if cont >= 1:
    print(f'O número 9 aparece {cont} vezes')
else:
    print('O número 9 não aparece na lista.')
if 3 in tupla:
    print(f'O numero 3 aparece a primeira vez na posição {tupla.index(3)}.')
else:
    print('O número 3 não aparece em nenhuma posição.')
print(f'Os números pares foram {par}')

