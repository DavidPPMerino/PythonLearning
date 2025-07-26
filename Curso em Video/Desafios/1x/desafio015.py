""" Enunciado:
        Escreva um programa que pergunte a quantidade de Km percorridos
        por um carro alugado e a quantidade de dias pelos quais ele foi
        alugado.
        Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
        e R$0,15 por Km rodado.
"""

" V1.0 "
# print('='*10,'Calculadora de aluguer de carros','='*10)
# d = int(input('Quantos dias teve o carro: '))
# km = float(input('Quantos kms conduziu: '))
# pd = d*60
# pkm = km*0.15
# tt = pd+pkm
# print('Voçê teve o carro durante {} dias e percorreu {}kms.'.format(d,km))
# print('O valor para os {} dias é de {} e para os {}kms é de {} totalizando {:.2f} por todo o aluguer'.format(d,pd,km,pkm,tt))

""" Resolução Curso em Video """
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a paga é de R${pago:.2f}')