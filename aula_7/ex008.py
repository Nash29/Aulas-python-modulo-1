#Escreva um programa que leia um valor em metros e o exiba convetido em centimetro e milimetro
v = float(input('Digite o valor em Metros: '))
cm = v * 100
mm = v * 1000
print('O valor convertido para CM será de {} e para MM será de {}'.format(cm,mm))