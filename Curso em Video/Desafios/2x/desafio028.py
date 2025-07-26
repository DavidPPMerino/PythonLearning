'''from random import randrange
import emoji

n = randrange(0, 5)
x = int(input('Escolha um numero entre 0 e 5: '))
if x == n:
    print(emoji.emojize(f'Acertou o numero correto era {n} :star_struck:', language='alias'))
else:
    print(emoji.emojize(f'Infelizmente não acertou :sad_but_relieved_face:, o numero correcto era {n}', language='alias'))'''

from random import randint
from time import sleep
import emoji

n = randint(0, 5)
print('>--=--<'*7)
print('Vou pensar num número entre 0 e 5. Tenta adivinhar...')
print('>--=--<'*7)
x = int(input('Qual foi o numero que eu pensei? '))
print('A Comparar...'.center(49, ' '))
sleep(3)
if x == n:
    print(emoji.emojize(f'Acertou o numero correto era {n} :star_struck:', language='alias'))
else:
    print(emoji.emojize(f'Infelizmente não acertou :sad_but_relieved_face:, o numero correcto era {n}', language='alias'))
