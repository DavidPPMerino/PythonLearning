""" Enunciado:
        Escreva um programa que faça o computador 'pensar' em um número
        inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
        foi o número escolhido pelo computador.
        O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

" V1.0 "
from random import randrange
import emoji

# n = randrange(0, 5)
# x = int(input('Escolha um numero entre 0 e 5: '))
# if x == n:
#     print(emoji.emojize(f'Acertou o numero correto era {n} :star_struck:', language='alias'))
# else:
#     print(emoji.emojize(f'Infelizmente não acertou :sad_but_relieved_face:, o numero correto era {n}', language='alias'))


""" Resolução Curso em Video """
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
