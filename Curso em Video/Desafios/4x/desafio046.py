""" Enunciado:
        Faça um programa que mostre na tela uma 'contagem regressiva' para
        o estouro de fogos de artifício, indo de '10 até 0', com uma pausa de 1 segundo entre eles.
"""

" V1.0 "
# from time import sleep as slp
#
#
# print('\033[1;31m-'*16,'\033[4;33mContagem para Fogo de Artifício\033[m','\033[1;31m-\033[m'*17)
# str(input('Carregue enter para iniciar a contagem: '))
# for c in range(10, 0, -1):
#     print(f'{c:^40}')
#     slp(1)
# print('Bum Bum Bum')

""" Resolução Curso em Video """
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POOOW!')