#Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros.

m = float(input('Digite a metragem: '))
print('{:.0f} metros tem {:.0f}cm, e {:.0f}mm.'.format(m, m*100, m*1000))

#Correto! :D
#Adicionando mais conversões.

print('{}Quilômetro(km) \n{}Hectómetro(hm) \n{}Decâmetro(dam)'
      ' \n{}Decímetro(dm)'.format(m/1000, m/100, m/10, m*10))