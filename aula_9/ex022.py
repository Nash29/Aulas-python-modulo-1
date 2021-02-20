# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todos as letras maiusculas
# O nome com todas minusculas
# Quantos letras ao todos (sem considerar espaços)
# quantos letras tem o primeiro nome

nome = input('Digite seu nome: ')
print('Seu nome em maiúculas é {}'.format(nome.upper()))# Deixa tudo em MAIUSCULO
print('Seu nome em minusculas é {}'.format(nome.lower()))# Deixa tudo em minusculo
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))# Tira os espaços das laterais - a quantidade de espaços NAO PRECISA ESPECIFICAR
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # Mostra quantas letras tem seu primeiro nome