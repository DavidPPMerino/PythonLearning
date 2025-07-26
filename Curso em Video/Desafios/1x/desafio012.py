""" Enunciado:
        Faça um algoritmo que leia o preço de um produto e mostre seu novo
        preço, com 5% de desconto.
"""

" V1.0 "
# print('===== Calculadora de 5% de desconto =====')
# n = float(input('Qual é o preço: '))
# x = float(input('Qual a percentagem: '))
# menos5 = n-(n*x/100) #n-(n*5/100)
# print('{:.2f} com {}% de desconto fica a {:.2f}'.format(n, x, menos5))

""" Resolução Curso em Video """
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')