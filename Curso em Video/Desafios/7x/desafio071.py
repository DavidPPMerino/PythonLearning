""" Enunciado:
        Crie um programa que simule o funcionamento de um 'caixa eletrônico'.
        No início, pergunte ao usuário qual será o 'valor a ser sacado'
        (número inteiro) e o programa vai informar quantas 'cédulas' de cada
        valor serão entregues.

        OBS: Considere que o caixa possui cédulas de 'R$50', 'R$20', 'R$10' e 'R$1.'
"""

" V1.0 "
print('-=' * 20 + '-')
print(f'{'Caixa Eletrônico':^41}')
print('-=' * 20 + '-')
amount = int(input('Que valor quer levantar? R$'))

note50 = amount // 50
amount = amount % 50
note20 = amount // 20
amount = amount % 20
note10 = amount // 10
amount = amount % 10
note5 = amount // 5
amount = amount % 5
note1 = amount // 1
print('-=' * 20 + '-')
if note50 != 0:
        print(f'Total de {note50} cédulas de R$50')
if note20 != 0:
        print(f'Total de {note20} cédulas de R$20')
if note10 != 0:
        print(f'Total de {note10} cédulas de R$10')
if note5 != 0:        
        print(f'Total de {note5} cédulas de R$5')
if note1 != 0:
        print(f'Total de {note1} cédulas de R$1')
print('-=' * 20 + '-')
print('Volte sempre. Tenha um bom dia!')