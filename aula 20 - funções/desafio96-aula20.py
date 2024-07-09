"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular(largura e comprimento) e mostre a área do terreno.
"""
texto = 'Controle de terrenos'
quant_caracteres = len(texto)
print(texto)
print('—' * quant_caracteres)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))


def área(a, b):
    s = a * b
    print(f'A área do seu terreno {a} x {b} é de {s}m².')


área(largura, comprimento)

#Corrreto! :D