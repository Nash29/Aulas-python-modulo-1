# Desenvolva um programa que pergunta a destancia de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas

km = float(input('Digite a distancia percorrida: '))

if km <= 200:
    valor = km * 0.50
    print('Você tera que pagar R${}'.format(valor))
else:
    valor = km * 0.45
    print('Você tera que pagar R${}'.format(valor))