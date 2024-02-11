# Parte pratica
'''nome = str(input('Digite seu nome: ')).upper()
if nome == 'RENATO':
    print('Renato em latim é "renascido das cinzas".')
else:
    print('Eu não sei o significado do seu nome.')
print('Bom dia, {}!'.format(nome.capitalize()))
print('==FIM==')
'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda note: '))
m = (n1 + n2) / 2
if m >= 5:
    print('Parabéns! Sua média foi {:.1f} e você foi aprovado!'.format(m))
else:
    print('Você foi reprovado! Sua média foi {:.1f}, tente novamente!'.format(m))

# Ou
print('Parabéns! Você foi aprovado!' if m >= 5 else 'Você foi reprovado!')  # Condição simplificada.
