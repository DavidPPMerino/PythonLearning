""" Enunciado:
Faça um 'mini-sistema' que utilize o 'Interactive Help' do 'Python'.
O usuário vai digitar o 'comando' e o 'manual' vai aparecer. Quando o usuário
digitar a palavra 'FIM', o programa se 'encerrará.
'OBS:' use 'cores'.
"""

" V1.0 "
# def titulo(ttl, cor):
#     print("\033[0m")
#     print(f'\033[{cor}m' + '~' * (len(ttl)+4) +'\033[0m')
#     print(f'\033[{cor}m' + f'{ttl}'.center(len(ttl)+4) +'\033[0m')
#     print(f'\033[{cor}m' + '~' * (len(ttl)+4)+'\033[0m')
#     print("\033[0m")


# while True:
#     titulo("Sistema de Ajuda PyHelp", "42;30;1")
#     check = input("\033[mFunção ou Biblioteca → ").lower().strip()
#     if check != "fim":
#         titulo(f"Acessando o manual do comando '{check}'", "44;30;1")
#         print("\033[47m")
#         help(check)
#     else:
#         titulo("ATÉ LOGO", "41;1;30")
#         break

""" Resolução Curso em Video """
from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[;30m'       # 6 - branco
    )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
    

# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
