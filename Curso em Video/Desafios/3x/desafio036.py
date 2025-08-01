""" Enunciado:
        Escreva um programa para aprovar o empréstimo bancário para a compra
        de uma casa. Pergunte o 'valor da casa', o 'salário' do comprador e
        em 'quantos anos' ele vai pagar.
        A prestação mensal, não pode exceder 30% do salário ou então o
        empréstimo será negado.
"""

" V1.0 "
# from time import sleep as slp
#
# print('\033[1;31m-'*10,'\033[4;33mSimulador de Crédito\033[m','\033[1;31m-\033[m'*10)
# valor = float(input('\033[1;33mQual o valor da casa?\033[m \033[32m€\033[m '))
# ord = float(input('\033[1;33mQual o seu ordenado?\033[m \033[32m€\033[m '))
# ano = int(input('\033[1;31mEm quantos anos quer pagar?\033[2;31m \033[1;4;31;43m'))
# print(f'A analizar o seu pedido de crédito...'.center(42),'\033[m')
# slp(3)
# prest = valor / (ano * 12)
# esf =  prest / ord * 100
# print('\033[1;4;31m','Prestação Calculada'.center(41),'\033[m')
# slp(1)
# print(f'\033[33mO valor da sua prestação será de \033[31m€{prest:.2f} \033[33mpor mês\033[m')
# print(f'\033[1;4;31;43m', f'A analizar a sua taxa de esforço...'.center(41),'\033[m')
# slp(3)
#
# if esf >= 30:
#     print(f'\033[1;4;31m', 'CRÉDITO RECUSADO!'.center(41),f'\033[m\n\033[33mInfelizmente para comprar o imóvel no valor de \033[31m€{valor:.2f}\033[m \033[33mem\033[m \033[31m{ano} \033[33m{'ano' if ano == 1 else 'anos'},\nA sua taxa de esforço será de \033[31m{esf:.2f}%\033[m')
# else:
#     print(f'\033[1;4;32m','CRÉDITO APROVADO!'.center(41),f'\033[m\n\033[33mParabéns o seu credito foi aprovado\nA sua prestação será de \033[31m€{prest:.2f}\033[m \033[33mdurante\033[m \033[31m{ano*12} meses ')


""" Resolução Curso em Video """
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos.', end='')
print(f' a prestação será de R${prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')