# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

import random
aluno = random.randint(1, 4)

for i in range(4):
    nome = input('Digite o nome do aluno {} : '.format(i+1))

if aluno == 1:
    print('O aluno escolhido foi {}!'.format(nome))
elif aluno == 2:
    print('O aluno escolhido foi {}!'.format(nome))
elif aluno == 3:
    print('O aluno escolhido foi {}!'.format(nome))
else:
    print('O aluno escolhido foi {}!'.format(nome))