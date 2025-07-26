""" Enunciado:
        Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
        mostre quantos Dólares ela pode comprar.

        Considere US$1.00 = R$3.27
"""

" V1.0 "
# print('===== Cambio real para dolares =====')
# n = float(input('Escreva quantos reais quer converter: '))
# brl = float(input('Escreva a taxa de cambio atual: '))
# usd = n/brl
# print('Com {:.2f} reais conseguiria comprar {:.2f} dolares.'.format(n, usd))

""" Resolução Curso em Video """
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')