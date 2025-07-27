""" Enunciado:
        Escreva um programa que leia 'dois números' inteiros e compare-os,
        mostrando na tela uma mensagem:
        - O primeiro valor é maior
        - O segundo valor é maior
        - Não existe valor maior, os dois são iguais
"""

" V1.0 "
# print('\033[1;31m-'*10,'\033[4;33mConversor de Números\033[m','\033[1;31m-\033[m'*10)
# num1 = int(input('\033[0;33mEscreva um número inteiro: '))
# print('\033[1;31m-'*42)
# num2 = int(input('\033[0;33mEscreva outro número inteiro: '))
# print('\033[1;31m-'*42)
#
# print('\033[1;31m-'*10,'\033[33mNúmeros selecionados\033[m','\033[1;31m-\033[m\033[1;31m'*10)
# print(f' \033[1;4;33m{num1}\033[m \033[1;31m||\033[m \033[1;4;33m{num2}\033[m \033[1;31m'.center(83,'.'))
# print('')
# if num1 > num2:
#     print(f'\033[33mO \033[31m{num1} \033[33mé o maior dos números!')
# elif num1 < num2:
#     print(f'\033[33mO \033[31m{num2} \033[33mé o maior dos números!')
# else:
#     print(f'\033[33mAmbos os números são \033[31miguais\033[33m!')

""" Resolução Curso em Video """
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')