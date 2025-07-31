""" Enunciado:
        Crie um programa que simule o funcionamento de um 'caixa eletrônico'.
        No início, pergunte ao usuário qual será o 'valor a ser sacado'
        (número inteiro) e o programa vai informar quantas 'cédulas' de cada
        valor serão entregues.

        OBS: Considere que o caixa possui cédulas de 'R$50', 'R$20', 'R$10' e 'R$1.'
"""

" V1.0 "
# print('-=' * 20 + '-')
# print(f'{'Caixa Eletrônico':^41}')
# print('-=' * 20 + '-')
# amount = int(input('Que valor quer levantar? R$'))

# note50 = amount // 50
# amount = amount % 50
# note20 = amount // 20
# amount = amount % 20
# note10 = amount // 10
# amount = amount % 10
# note1 = amount // 1
# print('-=' * 20 + '-')
# if note50 != 0:
#     print(f'Total de {note50} cédulas de R$50')
# if note20 != 0:
#     print(f'Total de {note20} cédulas de R$20')
# if note10 != 0:
#     print(f'Total de {note10} cédulas de R$10')
# if note1 != 0:
#     print(f'Total de {note1} cédulas de R$1')
# print('-=' * 20 + '-')
# print('Volte sempre. Tenha um bom dia!')

""" Resolução Curso em Video """
print('=' * 30)
print(f'{'BANCO CEV':^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
                print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
                céd = 20
        elif céd == 20:
                céd = 10
        elif céd == 10:
                céd = 1
        totcéd = 0
    if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
