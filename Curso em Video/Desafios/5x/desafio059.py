""" Enunciado:
[ 1 ] Somar             |    Crie umm programa que leia dois valores e mostre
[ 2 ] Multiplicar       |    um menu como o ao lado na tela:
[ 3 ] Maior             |    Seu programa deverá realizar a operação
[ 4 ] Novos Números     |    solicitada em cada caso.
[ 5 ] Sair do programa  |
"""

" V1.0 "
# programa = 's'
# while programa == 's':
#     n1 = float(input('Primeiro valor: '))
#     n2 = float(input('Segundo valor: '))
#     numeros = 's'
#     while numeros == 's':
#         escolha = int(input('''MENU:
#         [ 1 ] Somar
#         [ 2 ] Multiplicar
#         [ 3 ] Maior
#         [ 4 ] Novos valores
#         [ 5 ] Sair do Programa
#         Escolha a sua opção: '''))
#
#         if escolha == 1:
#             print(f'{n1} + {n2} = {n1 + n2}')
#
#         elif escolha == 2:
#             print(f'{n1} * {n2} = {n1 * n2}')
#
#         elif escolha == 3:
#             if n1 > n2:
#                 print(f'{n1} é maior que {n2}')
#             else:
#                 print(f'{n2} é maior que {n1}')
#
#         elif escolha == 4:
#             print('Escolha os seus novos numeros: ')
#             numeros = 'n'
#
#         elif escolha == 5:
#             print('A sair do programa...')
#             numeros = 'n'
#             programa = 'n'
#
#         else:
#             print('Opção Invalida! Tente novamente.')

""" Resolução Curso em Video """

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    print('=-=' * 10)
    if opção == 1:
        soma = n1 + n2
        print(f' A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'o resultado de {n1} x {n2} é {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')