""" Enunciado:
Faça um 'mini-sistema' que utilize o 'Interactive Help' do 'Python'.
O usuário vai digitar o 'comando' e o 'manual' vai aparecer. Quando o usuário
digitar a palavra 'FIM', o programa se 'encerrará.
'OBS:' use 'cores'.
"""

" V1.0 "
def titulo(ttl, cor):
    print("\033[0m")
    print(f'\033[{cor}m' + '~' * (len(ttl)+4) +'\033[0m')
    print(f'\033[{cor}m' + f'{ttl}'.center(len(ttl)+4) +'\033[0m')
    print(f'\033[{cor}m' + '~' * (len(ttl)+4)+'\033[0m')
    print("\033[0m")


while True:
    titulo("Sistema de Ajuda PyHelp", "42;30;1")
    check = input("\033[mFunção ou Biblioteca → ").lower().strip()
    if check != "fim":
        titulo(f"Acessando o manual do comando '{check}'", "44;30;1")
        print("\033[47m")
        help(check)
    else:
        titulo("ATÉ LOGO", "41;1;30")
        break
