""" Enunciado:
        Faça um programa que leia o ano de nascimento de um jovem e informe,
        de acordo com sua idade, se ele 'ainda vai se alista' ao serviço
        militar, se é a 'hora de se alistar' ou se já 'passou do tempo' do
        alistamento.
        Seu programa também deverá mostrar o tempo que falta ou que passou
        do prazo.
"""

" V1.0 "
# from datetime import date
# curyear = date.today().year
#
# print('\033[1;31m-'*10,'\033[4;33mCalculadora de Alistamento\033[m','\033[1;31m-\033[m'*10)
# birth = int(input('\033[0;33mEscreva o seu ano de nascimento: '))
# idd = curyear - birth
# saldo = 18 - idd if idd < 18 else idd - 18
# print('\033[1;31m-'*48)
# if idd >= 18:
#     print('\033[1;31m1\033[m \033[33m= \033[32mSim'.center(60))
#     print('\033[1;31m2\033[m \033[33m= \033[32mNão'.center(60))
#     ynlist = int(input('\033[33mSe já se alistou escreva \033[1;31m1\033[0;33m caso contrario escreva \033[1;31m2\033[33m: '))
#     print('\033[1;31m-'*48)
#     print(saldo)
#     if ynlist == 1:
#         print('\033[32mObrigado \033[33mpor ter cumprido o seu dever militar!')
#     elif idd > 18:
#         print(f'\033[1;4;31mAtenção!!!\033[0;33m Já deveria ter feito o seu alistamento há \033[1;31m{idd - 18}\033[0;33m {'ano' if idd - 18 < 2 else 'anos'}!')
#     else:
#         print(f'\033[1;4;31mAtenção!!!\033[0;33m Está na altura de fazer o seu alistamento!')
# else:
#     print(saldo)
#     print(f'\033[1;4;31mAtenção!!!\033[0;33m Faltam \033[1;31m{18 - idd}\033[0;33m {'ano' if idd - 18 < 2 else 'anos'} o seu alistamento!')

""" Resolução Curso em Video """
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
