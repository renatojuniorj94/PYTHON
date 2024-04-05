soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n

if cont == 0:
    print('Você não digitou nenhum número par')
else:
    print('Você informou {} números pares e a soma foi {}'.format(cont, soma))