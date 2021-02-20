#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
Sal = float(input('Digite o seu salário: '))
newSal = round(Sal + (Sal*15)/100, 2)
print('Seu novo salário com o aumento de 15% é de R${}'.format(newSal))