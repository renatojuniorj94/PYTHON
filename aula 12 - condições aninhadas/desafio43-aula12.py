"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
# Ou peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso ideal.'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {:.2f} e você está no peso ideal.'.format(imc))
elif 25 >= imc and imc < 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso.'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é {:.2f} e você está obeso.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e seu quadro é de obesidade mórbida'.format(imc))

# Correto! :D
