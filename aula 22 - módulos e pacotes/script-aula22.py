#from uteis import fatorial, dobro
import uteis
num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')