""" Enunciado:
Crie um programa onde o usuário possa digitar vários 'valores numéricos' e
cadastre-os em uma 'lista'.
Caso o número já exista lá dentro, ele 'não será adicionado'.
No final, serão exibidos todos os 'valores únicos' digitados, em 'ordem crescente'.
"""
# nums = []
# while True:
#     check = ""
#     num = int(input("Escreva um valor: "))
#     if num in nums:
#         print("Valor duplicado! Não vou adicionar...")
#     else:
#         print("Valor adicionado com sucesso...")
#         nums.append(num)
#     while check not in ("S", "N"):
#         check = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
#     if check == "N":
#         break
# nums.sort()
# print("-=" * 15 + "-")
# print(f"Você digitou os valores {nums}")

""" Resolução Curso em Video """
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
    print('-=' * 30)
    números.sort()
    print(f'Você digitou os valores {números}')
    