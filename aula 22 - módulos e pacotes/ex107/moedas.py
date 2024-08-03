def moeda(num):
    ponto_flutuante = f"{num:.2f}"
    num = ponto_flutuante
    real_string = str(num).replace('.', ',')
    real_formatado = 'R$ {}'.format(real_string)
    return real_formatado


def aumentar(num):
    return num + ((num * 10) / 100)


def diminuir(num):
    return num - ((num * 13) / 100)


def dobra(num):
    return num * 2


def metade(num):
    return num / 2