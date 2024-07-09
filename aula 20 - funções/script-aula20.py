def mensagem(msg):
    print('—' * 30)
    print(msg)
    print('—' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')


#Programa principal
#Função mensagem()
mensagem('COPA LIBERTADORES')
mensagem('CAMPEONATO BRASILEIRO')
mensagem('COPA DO BRASIL')

#Função soma()
soma(b=4, a=5)  # Se não especificar, automaticamente o primeiro número fica dentro de "A" e o segundo dentro de "B"
soma(8, 9)
soma(2, 1)


def contador(*num):  # '*' está desempacotando diversos números
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


"""
def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')
"""


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)


def somar(*valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')


somar(5, 2)
somar(2, 9, 4)
