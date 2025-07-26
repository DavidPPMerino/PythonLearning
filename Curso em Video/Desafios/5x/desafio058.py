""" Enunciado:
        Melhore o jogo do desafio 028 onde o computador vai pensar em um numero
        entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
        mostrando no final quantos palpites foram necessários para vencer.
"""

" V1.0 "
# from random import randint
#
# continuar = 'S'
# while continuar in 'S':
#
#     computador = randint(0, 10)
#     jogador = int(11)
#     tentativas = 0
#
#     while jogador != computador:
#         jogador = int(input('Escreva um numero de 0 a 10: '))
#         prox = abs(computador - jogador)
#         if 0 <= jogador <= 10:
#             tentativas += 1
#             if prox == 1:
#                 print('Estás bem proximo!')
#             elif 3 > prox >= 1:
#                 print('Estás proximo!')
#             elif 6 > prox >= 3:
#                 print('Está morno!')
#             elif prox >= 6:
#                 print('Está frio')
#             elif computador == jogador:
#                 print(f'Acertaste, precisaste de {tentativas} tentativas para acertar.')
#         else:
#             print('Escolha invalida! Deves escolher entre 0 e 10!')
#
#     continuar = ' '
#     while continuar not in ('S', 'N'):
#         continuar = input('Quer continuar a jogar? [S/N] ').strip().upper()
#         if len(continuar) > 1 and continuar not in ('S', 'N'):
#             print('Opção invalida! Escolha S ou N para continuar ou parar!')
#         elif continuar == 'N':
#             print('Obrigado por jogares, vemo-nos numa proxima vez!')

""" Resolução Curso em Video """

from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
