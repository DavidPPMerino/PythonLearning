""" Enunciado:
        Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

" V1.0 "
# ano = int(input('Que ano quer confirmar se é Bissexto? Escreva 0 para analisar o ano atual: '))
# if str(ano).endswith('00'):
#     if ano % 400 == 0:
#         print(f'O ano {ano} é bissexto!')
#     else:
#         print(f'O ano {ano} não é bissexto!')
# else:
#     if ano % 4 == 0:
#         print(f'O ano {ano} é bissexto!')
#     else:
#         print(f'O ano {ano} não é bissexto!')

""" Resolução Curso em Video """
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')