def moeda(num):
    ponto_flutuante = f"{num:.2f}"
    num = ponto_flutuante
    real_string = str(num).replace('.', ',')
    real_formatado = 'R$ {}'.format(real_string)
    return real_formatado


def aumentar(num, porc, formatado=False):
    return num + ((num * porc) / 100) if formatado is False else moeda()


def diminuir(num, porc, formatado=False):
    return num - ((num * porc) / 100)


def dobra(num, formatado=False):
    return num * 2


def metade(num, formatado=False):
    return num / 2