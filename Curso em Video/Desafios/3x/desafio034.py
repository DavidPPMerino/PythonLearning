ord = float(input('Qual é o seu ordenado?: '))
if ord >= 1250:
    print(f'O seu salario com o aumento de 10% ficará em {ord+ord*10/100:.2f}€.')
else:
    print(f'O seu salario com o aumento de 15% ficará em {ord+ord*15/100:.2f}€. ')