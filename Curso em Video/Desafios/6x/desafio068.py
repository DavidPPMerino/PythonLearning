""" Enunciado:
        Faça um programa que jogue 'par ou impar' com o computador. O jogo
        só será interrompido quando o jogador 'PERDER', mostrando o total
        de vitórias consecutivas que ele conquistou no final do jogo.
"""

" V1.0  de 0 a 5"
from random import randint
print('-=' * 15 + '-')
print(f'{'VAMOS JOGAR PAR OU IMPAR':^31}')

count =  0
odd_even = ' '

while True:
    player = 6
    odd_even = ' '
    computer = randint(0, 5)

    print('-=' * 15 + '-')

    while player < 0 or player > 5:
        player = int(input('Escreva um valor de 0 a 5: '))
        sums = player + computer
        even = sums % 2 == 0

    while odd_even not in ('P','I'):
        odd_even = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print('-' * 31)
    print(f'Você jogou {player} e o computador {computer}.', end=' ')

    if even:
        print(f'Total de {sums} DEU PAR')
    else:
        print(f'Total de {sums} DEU ÍMPAR')
    print('-' * 31)
    if odd_even == 'P' and even or odd_even == 'I' and not even:
        count += 1
        print('Você VENCEU!\nVamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break
print('-=' * 15 + '-')
print(f'GAME OVER! Você venceu {count} vezes')
