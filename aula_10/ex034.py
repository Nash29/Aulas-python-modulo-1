# Escreva um programa que pergunte o salario de um funcionaro e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
# Para os infeirores ou iguais, o aumento é de 15%

sal = float(input('Digite o seu salario: '))

if sal > 1250:
    newSal = sal + (sal * 10) / 100
    print('Seu novo salario sera de R${:.2f}'.format(newSal))
else:
    newSal = sal + (sal * 15) / 100
    print('Seu novo salario sera de R${:.2f}'.format(newSal))