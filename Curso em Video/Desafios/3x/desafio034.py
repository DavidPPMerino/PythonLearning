""" Enunciado:
        Escreva um programa que pergunte o salário de um funcionário e
        calcule o valor do seu aumento.
        Para salários superiores a R$1250,00, calcule um aumento de 10%.
        Para inferiores ou iguais, o aumento é de 15%.
"""

" V1.0 "
# ord = float(input('Qual é o seu ordenado?: '))
# if ord >= 1250:
#     print(f'O seu salario com o aumento de 10% ficará em {ord+ord*10/100:.2f}€.')
# else:
#     print(f'O seu salario com o aumento de 15% ficará em {ord+ord*15/100:.2f}€. ')

""" Resolução Curso em Video """
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora.')