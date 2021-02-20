print('\033[7;30mOla Mundo!\033[m')

# Primeiro tipo
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))

# Segundo tipo
nome = 'Murilo'
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Terceiro tipo
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('É um prazer te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

from datetime import date
ano = date.today().y