'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A - Quantos vezes apareceu o valor 9.
B - Em que posição foi digitado o primeiro valor 3.
C - Quais foram os números pares.
'''

cont = cont_par = 0
tupla = par = ()
for c in range(1, 5):
    num = int(input('Digite um número: '))
    tupla += num,
    if num == 9:
        cont += 1

    if num % 2 == 0:
        par += num,
        cont_par += 1

print(f'Você digitou os números {tupla}')
if cont >= 1:
    print(f'O número 9 aparece {cont} vezes')
else:
    print('O número 9 não aparece na lista.')
if 3 in tupla:
    print(f'O numero 3 aparece a primeira vez na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não aparece em nenhuma posição.')
if cont_par >= 1:
    print(f'Os números pares foram {par}')
else:
    print('Não existe número par na lista')

#Correto! :D
#Outra maneira de fazer:

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')