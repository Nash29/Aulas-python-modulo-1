# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

speed = float(input('Digite a velocidade do carro: '))

if speed > 80:
    print('Você foi multado')
    multa = (speed - 80) * 7;
    print('Você tera que pagar R${}'.format(multa))