#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: O numero 6.127 tem a parte inteira 6
import math
n1 = float(input('Digite um numero real: '))
n2 = math.floor(n1) # Aparece apenas a parte inteira
print('A parte inteira do numero {} é {}'.format(n1, n2))