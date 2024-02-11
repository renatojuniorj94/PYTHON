#Parte teórica
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é antigo!')

print('==FIM==')

# Ou
print('Carro novo' if tempo <= 3 else 'Carro velho')  # Isso é uma condição simplificada.
