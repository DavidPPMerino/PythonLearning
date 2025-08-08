""" Enunciado:
Crie um programa que vai gerar 'cinco números aleatórios e colocar em uma 
'tupla'.
Depois disso, mostra a 'listagem de números' gerados e tambem indique 
o 'menor' e o 'maior' valor que estão na tupla.
"""

" V1.0 "
# from random import randint

# n1 = randint(0, 10)
# n2 = randint(0, 10)
# n3 = randint(0, 10)
# n4 = randint(0, 10)
# n5 = randint(0, 10)
# nums = (n1, n2, n3, n4, n5)
# high = 0
# low = 0
# print("Os valores sorteados foram: ", end='')
# for i, num in enumerate(nums):
#     if i == 4:
#         print(num)
#     else:
#         print(num, end=' ')
#     if i == 0:
#         high = num
#         low = num
#     elif num > high:
#         high = num
#     elif num < low:
#         low = num
# # print(i)
# print(f"O maior valor sorteado foi {high}")
# print(f"O menor valor sorteado foi {low}")

""" Resolução Curso em Video """
from random import randint
números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), 
           randint(1,10))
print('Os valores sorteados fora: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')