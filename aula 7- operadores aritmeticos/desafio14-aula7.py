#Escreva um programa que converta uma temperatura digitada em ºc e converta para ºf.

c = float(input('Digite quantos graus ºC faz na sua cidade: '))
print('{}ºC convertido para Fahrenheit fica em {:.2f}ºF'.format(c, c * 1.8 + 32))

#Correto!
#Outra maneira de calcular:

#Na verdade não precisamos dos parênteses devido a ordem de precedência.
f = ((9 * c) / 5) + 32
print(f)