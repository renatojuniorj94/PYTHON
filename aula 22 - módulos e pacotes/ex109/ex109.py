def moeda(num):  # Função do desafio 109
    ponto_flutuante = f"{num:.2f}"
    num = ponto_flutuante
    real_string = str(num).replace('.', ',')
    real_formatado = 'R$ {}'.format(real_string)
    return real_formatado


#Correto! :D
#Outra maneira de fazer...


def moeda(num, real='R$ '):
    return f'{real}{num:>.2f}'.replace('.', ',')


def aumentar(num, porc, formatado=False):
    res = num + ((num * porc) / 100)
    return res if formatado is False else moeda(res)


def diminuir(num, porc, formatado=False):
    res = num - ((num * porc) / 100)
    return res if formatado is False else moeda(res)


def dobra(num, formatado=False):
    res = num * 2
    return res if not formatado else moeda(res)


def metade(num, formatado=False):
    res = num / 2
    return res if not formatado else moeda(res)