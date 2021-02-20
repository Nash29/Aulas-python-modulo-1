# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR
# Murilo lembra resto da divisão % = 0 par

num = int(input('Digite um numero inteiro: '))

if num % 2 == 0:
    print('O {} é um número PAR'.format(num))
else:
    print('O {} é um numero IMPAR'.format(num))