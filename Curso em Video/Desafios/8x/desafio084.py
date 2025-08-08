""" Enunciado:
Faça um programa que leia 'nome e peso' de 'várias pessoas', guardando tudo em 
uma 'lista'. No final, mostre:
a) 'Quantas' pessoas foram cadastradas.
b) Uma listagem com as pessoas mais 'pesadas'.
c) Uma listagem com as pessoas mais 'leves'.
"""

" V1.0 "
# people = []
# data = []
# heaviest = lightest = count = 0
# while True:
#     check = " "
#     data.append(str(input('Nome: ')))
#     data.append(float(input('Peso em Kg: ')))
#     people.append(data[:])
#     if not count:
#         heaviest = lightest = data[1]
#     else:
#         if data[1] < lightest:
#             lightest = data[1]
#         if data[1] > heaviest:
#             heaviest = data[1]
#     data.clear()
#     count += 1
#     while check not in "SN":
#         check = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
#     if check == "N":
#         break
# print("-=" * 25 + "-")
# print(f"No total, você registou {len(people)} pessoas.")
# print(f"O maior peso registado foi de {heaviest}Kg. Peso de: ", end="")
# for person in people:
#     if person[1] == heaviest:
#         print(person[0], end=" ")
# print()
# print(f"O menor peso registado foi de {lightest}Kg. Peso de: ", end="")
# for person in people:
#     if person[1] == int(lightest):
#         print(person[0], end=" ")

""" Resolução Curso em Video """
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')
