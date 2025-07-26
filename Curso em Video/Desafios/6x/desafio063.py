""" Enunciado:
        Escreva um programa que leia um número 'n' inteiro qualquer e mostre
        na tela os 'n' primeiros elementos de uma Sequência de Fibonacci.
        Ex:
        0 → 1 → 1 → 2 → 3 → 5 → 8
"""

" V1.0 "
# print(f'{' Sequência de Fibonacci ':=^040}')
# elem = int(input('Quantos elementos deseja mostrar?: '))
# count = 0
# fib = 0
# fib1 = 0
# fib2 = 0
# print(f'{fib}', end= ' ')
# while count != elem:
#     if count == 0:
#         count += 1
#     if count == 1:
#         fib += 1
#         count += 1
#         print(f'→ {fib}', end=' ')
#         fib1 = fib
#     if count == 2:
#         fib2 = fib1
#         count +=1
#         print(f'→ {fib}', end=' ')
#         fib1 = fib
#     else:
#         fib = fib1 + fib2
#         count += 1
#         print(f'→ {fib}', end=' ')
#         fib2 = fib1
#         fib1 = fib


""" Resolução Curso em Video """

print('-' * 30)
print('Sequência de Fibonacci'.center(30))
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' → FIM')
print('~' * 30)