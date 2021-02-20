# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
#Considere U$1,00 = R$3,27
valor = float(input('Digite quanto dinheiro você possui: '))
dolar = round(valor / 3.27, 2)# Deixa apenas 2 casas depois da virgula
print('Você podera compra {} Dolares'.format(dolar))