""" Enunciado:
        Crie um programa que leia o 'ano de nascimento' de 'sete pessoas'.
        No final, mostre quantas pessoas ainda nãoaatingiram a maioridade e
        quantas já são maiores.
"""

" V1.0 "
# from datetime import date
#
#
# cur_year = date.today().year
# maior = 0
# menor = 0
#
# for c in range(1,8):
#     ano = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
#     idade = cur_year - ano
#
#     if idade >= 18:
#     # if cur_year - ano >= 18:
#         maior += 1
#
#     else:
#         menor += 1
#
# if maior == c:
#     print(f'Todas as {maior} pessoas atingiram a maioridade!')
# elif menor == c:
#     print(f'Nenhuma das {menor} pessoas atingiu a maioridade')
# else:
#     print(f'{maior} pessoas já atingiram a maioridade e {menor} ainda nao atingiram!')

""" Resolução Curso em Video """
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'e também tivemos {totmenor} pessoas menores de idade')