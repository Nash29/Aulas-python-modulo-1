# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantos vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A'))) # Count: conta quantas vezes apareceu a letra A
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))# Find: pega a primeira posição da letra selecionada
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))# rfind: pega a ultima posição da letra selecionada