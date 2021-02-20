# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome // TRUE OR FALSE
nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))