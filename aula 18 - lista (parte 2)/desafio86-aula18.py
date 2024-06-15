"""
Crie um programa que crie uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite um valor na posição {[linha, c]}: '))
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')

#Correto! :D
#Outra maneira de fazer...

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite um valor na posição {[linha, c]}: '))
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end='')
    print()