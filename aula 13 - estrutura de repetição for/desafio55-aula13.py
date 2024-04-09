'''
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
'''

maximo = 0
minimo = float('inf')  # Inicializando com um valor muito grande
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > maximo:
        maximo = peso

    if peso < minimo:
        minimo = peso

print('O maior peso lido foi de {}kg.'.format(maximo))
print('O menor peso lido foi de {}kg.'.format(minimo))

#Explicação IA para o float('inf'):
'''
float('inf') é uma expressão em Python que cria um valor especial chamado "infinito" (infinito positivo). 
Essencialmente, ele representa um valor numérico que é maior do que qualquer outro valor numérico finito.

Quando você usa float('inf'), você está atribuindo à variável um valor que é tão grande que qualquer número real 
comparado a ele será considerado menor. Isso é útil em situações onde você precisa inicializar uma variável com um 
valor inicial que será atualizado para um valor real posteriormente, e você quer garantir que o valor inicial não 
afete as comparações.

Da mesma forma, você pode usar float('-inf') para representar o infinito negativo, que é um valor menor do que 
qualquer outro valor numérico finito.

Em resumo, float('inf') é usado para representar infinito positivo e float('-inf') é usado para representar infinito 
negativo em Python.'''

#Correto! :D
#Outra maneira de fazer:

maior2 = 0
menor2 = 0
for p in range(1,6):
    peso2 = float(input('Digite o peso da {}ª pessoa: '.format(p)))

    if p == 1:
        maior2 = peso2
        menor2 = peso2
    else:
        if peso2 > maior2:
            maior2 = peso2
        if peso2 < menor2:
            menor2 = peso2

print('O maior peso lido foi de {}kg.'.format(maior2))
print('O menor peso lido foi de {}kg.'.format(menor2))