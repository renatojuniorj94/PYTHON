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


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)