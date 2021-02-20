#Faça um ptrograma que leia um numero inteiro qualquer e mostre na tela a sua tabuada
n1 = int(input('Digite um número: '))
for i in range(11):
    print(i, "X", n1, "= {}".format(i*n1))