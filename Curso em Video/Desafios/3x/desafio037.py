""" Enunciado:
        Escreva um programa que leia um número inteiro qualquer e peça para
        o usuário escolher qual será a 'base de conversão:
        - 1 para binário
        - 2 para octal
        - 3 para hexadecimal
"""

" V1.0 ordem alterada para ficar mais organizado"
# print('\033[1;31m-'*10,'\033[4;33mConversor de Números\033[m','\033[1;31m-\033[m'*10)
# num = int(input('\033[33mEscreva um número inteiro: '))
# print('\033[1;31m-'*42)
# print('\033[31m1\033[m \033[33m= \033[32mOctal'.center(60))
# print('\033[31m2\033[m \033[33m= \033[32mBinário'.center(60))
# print('\033[31m3\033[m \033[33m= \033[32mHexadecimal'.center(60))
# base = int(input('\033[33mEscreva o número da base desejada: '))
# print('\033[1;31m-'*42)
# if base == 1:
#     print(f'\033[33m O número \033[31m{num} \033[33mconvertido para \033[32mOctal \033[33mé \033[31m{num:o}')
# elif base == 2:
#     print(f'\033[33m O número \033[31m{num} \033[33mconvertido para \033[32mBinário \033[33mé \033[31m{num:b}')
# elif base == 3 :
#     print(f'\033[33m O número \033[31m{num} \033[33mconvertido para \033[32mHexadecimal \033[33mé \033[31m{num:X}')
# else:
#     print('Selecionou uma opção invalida!')

""" Resolução Curso em Video """
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das base de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a{bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {bin(num)[2:]}')
elif opção == 3:
    print(f'{num} convervido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')