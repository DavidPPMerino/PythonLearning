""" Enunciado:
Faça um programa que leia '5 valores numéricos'e guarde-os em uma 'lista'.
No final, mostre qual foi o 'maior' e o 'menor' valor digitado e as suas 
respetivas 'posições' na lista.
"""
# list = []
# for count in range(0, 5):
#     list.append(int(input(f"Escreva um valor para a Posição {count}: ")))
# print('-=' * 15 + '-')
# print(f"Você escreveu os valores {list}")
# print(f"O maior valor digitado foi {max(list)} {'nas posições' if list.count(max(list)) > 1 else 'na posição'}", end=" ")
# for i, num in enumerate(list):
#     if num == max(list):
#         print(f'{i}... ', end=' ')
# print(f"\nO menor valor digitado foi {min(list)} {'nas posições' if list.count(min(list)) > 1 else 'na posição'}", end=" ")
# for i, num in enumerate(list):
#     if num == min(list):
#         print(f"{i}... ", end=" ")

""" Resolução Curso em Video """
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
    
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
