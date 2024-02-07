#Exibindo do 9 ao 13
frase = 'Curso em Vídeo Python'
print(frase[9:14])

#9 ao 21, pulando de 2 em 2
print(frase[9:21:2])

#Do zero ao 5
print(frase[:5])

#Do 15 até o final
print(frase[15:])

#Do 9 até o final, pulando de 3 em 3.
print(frase[9::3])

#Lendo quantos caracteres possuí uma string.
print(len(frase))

#Exibindo quantidade de  letras "o" (minusculas) possui uma string.
print(frase.count('o'))

#Exibindo quantidade de letras "o" dentro de uma string.
print(frase.count('o', 0, 13))

#A partir de qual pedaço da string ele encontrou "deo"
#Se a palavra ou letra não existir na string, ele retorna -1
print(frase.find('deo'))

#Existe "Curso" em frase? Retorna 'True' ou 'False'
print('Curso' in frase)

#Substituindo "Python" por "Android"
print(frase.replace('Python', 'Android'))

#Convertendo toda frase para maiúsculo
print(frase.upper())

#Convertendo para minusculo
print(frase.lower())

#Deixando somente o primeiro caractere em maiúsculo e convertendo os demais em minusculo.
print(frase.capitalize())

#Fazendo capitalize palavra por palavra.
print(frase.title())

#Removendo espaços em branco inúteis no ínicio e no fim da frase. Ex:    Aprenda Python
print(frase.strip())

#Removendo espaços inúteis da direita.
print(frase.rstrip())

#Removendo espaços inúteis da esquerda.
print(frase.lstrip())

#Dividindo strings conforme os espaços.
print(frase.split())

#Separando letra por letra com traço. '-'
print('-'.join(frase))

#Tranformando frase em lista depois separando com '-' usando método join().
print('-'.join(frase.split()))
