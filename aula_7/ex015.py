# Faça um programa sobre aluguel de carro, informando quantos dias ele foi alugado, quantos quilometros foi rodado
# e mostre o total a pagar, sabendo que o carro custa R$60 por dia e R$0,15 KM rodado
dias = int(input('Digite quantos dias o carro foi alugado: '))
KM = float(input('Digite quantos Km você rodou com o carro: '))
Val_dia = dias * 60
Val_Km = KM * 0.15
total = round(Val_dia + Val_Km, 2)
print('O total a pagar é de R${}'.format(total))