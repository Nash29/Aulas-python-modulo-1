# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta, pinta um area de 2m².

Larg = float(input('Digite a Largura da parede (em Metros): '))
Alt = float(input('Digite a Altura da parede (em Metros): '))
area = Larg * Alt
total = area / 2
print('A area da parede é de {}m²'.format(area))
print('A quantidade de tinta necessario é de {} litros de tinta'.format(total))