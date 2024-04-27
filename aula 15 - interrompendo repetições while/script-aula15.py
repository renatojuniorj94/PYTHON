#Interrompendo repetições while utilizando 'break'
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 000:
        break
    s += n
#Aprendemos também a utilizar f'strings
print(f'A soma vale {s:=^15}')

