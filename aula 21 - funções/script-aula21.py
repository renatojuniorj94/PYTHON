#Interactive Help (Ajuda interativa)
help(print)
print('—' * 100)
print(input.__doc__)
#Ou
help(input)


#Docstring (Nossa documentação)
def contador(i, f, p):
    """
    — > Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Função criada por Renato Junior (https://github.com/renatojuniorj94)
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)

#Parâmetros opcionais
'''Se em uma função deixarmos um parâmetro em branco ele será ignorado sem apresentar
erro na execução do código.'''


def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
print()

#Escopo de variáveis
'''-Quando uma variável é declarada dentro de uma função, laço de repetição ou semelhante, ele só pode
    ser usado lá. (Variável/escopo local)
    -Quando uma variável pode ser usada em todo programa, dentro ou fora de uma função
    ou laço de repetição. (Variável/escopo global)'''


def teste(b):
    global a  # Agora essa é a variável global
    a = 8  # Variável/escopo local
    b += 4  # Variável/escopo local
    c = 2  # Variável/escopo local
    print(f'"A" dentro vale {a}')
    print(f'"B" dentro vale {b}')
    print(f'"C" dentro vale {c}')


a = 5  # Variável/escopo global
teste(a)
print(f'"A" fora vale {a}')
print()

#Retorno de valores/resultados (return)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print()

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


valor = int(input('Digite um número: '))
print(par(valor))
if par(valor):
    print('É par!')
else:
    print('É impar!')