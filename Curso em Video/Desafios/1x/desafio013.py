""" Enunciado:
        Faça um algoritmo que leia o salário de um funcionário e mostre o
        seu novo salário, com 15% de aumento.
"""

" V1.0 "
# print('===== Aumento de salario de 15% =====')
# n = float(input('Qual é o seu salario atual: '))
# x = float(input('Qual a percentagem: '))
# s15 = n+(n*x/100) #n+(n*15/100)
# print('O seu salario de {:.2f} quando sofrer um aumento de {}% ficará em {:.2f}'.format(n, x, s15))

""" Resolução Curso em Video """
salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print(f'Um funcionário que ganhava R${salário:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')