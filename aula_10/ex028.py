# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o
# usario tentar descobrir qual foi o numero escolhido pelo computador
# O pregrama devera escrever na tela se o usuario venceu ou perdeu

import random

num = random.randint(0, 5)
val = int(input('Digite o número que você acha que o computador escolheu: '))
if val == num:
    print('Parabéns, você venceu ;)')
else:
    print('O computador venceu :(')


