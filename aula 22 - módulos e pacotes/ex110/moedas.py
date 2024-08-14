"""
def moeda(num):
    ponto_flutuante = f"{num:.2f}"
    num = ponto_flutuante
    real_string = str(num).replace('.', ',')
    real_formatado = 'R$ {}'.format(real_string)
    return real_formatado


def aumentar(num, porc):
    return num + ((num * porc) / 100)


def diminuir(num, porc):
    return num - ((num * porc) / 100)


def dobra(num, formatado=False):
    return num * 2


def metade(num):
    return num / 2


def resumo(n, aumento, redução):
    frase = '    RESUMO DO VALOR    '
    print('—' * len(frase))
    print(frase)
    print('—' * len(frase))
    print(f'{"Preço analisado:"} \t{moeda(n)}')
    print(f'{"Dobro do preço:"} \t{moeda(dobra(n))}')
    print(f'{"Metade do preço:"} \t{moeda(metade(n))}')
    print(f'{"Aumento de "}{aumento}{"%:"} \t{moeda(aumentar(n, aumento))}')
    print(f'{"Redução de "}{redução}{"%:"} \t{moeda(diminuir(n, redução))}')
"""

#Correto! :D
#Outra maneira de fazer...


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço= 0, taxaa=10, taxar=5):  # Se não for especificado, o preço padrão é 0, taxa de aumento é 10 e taxa
    # de redução é 5.
    print('—' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('—' * 30)
    print(f'Preço analisado: \t{moeda(preço, True)}')
    print(f'Dobro do preço: \t{dobra(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('—' * 30)