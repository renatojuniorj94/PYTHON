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


def metade(num):
    return num / 2

#Correto! :D
#Outra maneira de fazer...


def aumentar(preço, taxa):
    res = preço + (preço * taxa / 100)  # Calculo de aumento de porcentagem.
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa / 100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res
