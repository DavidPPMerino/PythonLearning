# n = int(input('Escreva um número inteiro: '))
# multiplos = 0
# if n >= 2:
#     for i in range(1,n+1):
#         if n % i == 0:
#             multiplos += 1
#     if multiplos ==2:
#         print(f'O número {n} é primo')
#     else:
#         print(f'O número {n} não é primo')
# else:
#     print(f'O número {n} não é primo')
#
tot = 0
n = int(input('Digite um numero: '))
for c in range(1, n+1):
    if n % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
