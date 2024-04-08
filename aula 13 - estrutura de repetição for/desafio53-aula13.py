'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''

print('='*30)
print('{:^30}'.format('JOGO DO PALÍNDROMO'))
print('='*30)

#Strip = Removendo espaços no ínicio e no fim da frase.
#Upper = Transformando letras em maiúsculas.
frase = input('Digite uma palavra, frase ou nome: ').strip().upper()
#Split = Dividindo strings pelo espaço entre elas
palavras = frase.split()
#Join = Juntando strings
juntando = ''.join(palavras)
inverso = ''

#Primeiro -1 = Começa lendo a última letra.
#Segundo -1 = Começa lendo antes da primeira.
#Terceiro -1 = Começando de trás para frente.
#Usamos o laço de repetição FOR para inverter a ordem das letras.
for letra in range(len(juntando) - 1, -1, -1):
    inverso += juntando[letra]

print('O inverso de {} é {}'.format(frase, inverso))

if inverso == juntando:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')

# Fazendo sem FOR
frase = input('Digite uma palavra, frase ou nome: ').strip().upper()
palavras = frase.split()
juntando = ''.join(palavras)
inverso = juntando[::-1]
print('O inverso de {} é {}'.format(juntando, inverso))

if inverso == juntando:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')
