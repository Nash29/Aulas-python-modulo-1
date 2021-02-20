# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o preço do produto: '))
newP = round(preco - (preco * 5)/100, 2) # Coloca 2 casas depois da virgula
print('O novo preço do produto com 5% de desconto é de {}'.format(newP))