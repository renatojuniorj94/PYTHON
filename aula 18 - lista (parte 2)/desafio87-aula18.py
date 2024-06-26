"""
Aprimore o desafio anterior, mostrando no final:
A - A soma de todos os valores pares digitados.
B - A soma dos valores da terceira coluna.
C - O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = colTres = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição {[l, c]}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
print('-=' * 30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
print('-=' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

#Correto! :D
#Outra maneira de fazer...

#Para somar os números da terceira coluna:
for t in range(0, 3):
    colTres += matriz[l][2]
print(f'A soma da coluna três é {colTres}')
#Maior número da segundo linha:
for linha in range(0, 3):
    if linha == 0:
        maior = matriz[1][linha]
    elif matriz[1][linha] > maior:
        maior = matriz[1][linha]
print(f'O maior número da segunda linha é {maior}')