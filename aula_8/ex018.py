#Faça um programa que leia um triangulo qualquer e msotre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input('Digite o ângulo que deseja: '))
sen = math.sin(math.radians(angulo)) # Tem que passar para Radianos
cos = math.cos(math.radians(angulo)) # Tem que passar para Radianos
tan = math.tan(math.radians(angulo)) # Tem que passar para Radianos
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))