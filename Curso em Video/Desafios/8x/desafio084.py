""" Enunciado:
Faça um programa que leia 'nome e peso' de 'várias pessoas', guardando tudo em 
uma 'lista'. No final, mostre:
a) 'Quantas' pessoas foram cadastradas.
b) Uma listagem com as pessoas mais 'pesadas'.
c) Uma listagem com as pessoas mais 'leves'.
"""
people = []
data = []
heaviest = lightest = count = 0
while True:
    check = " "
    data.append(str(input('Nome: ')))
    data.append(int(input('Peso em Kg: ')))
    people.append(data[:])
    if not count:
        heaviest = lightest = data[1]
    else:
        if data[1] < lightest:
            lightest = data[1]
        if data[1] > heaviest:
            heaviest = data[1]
    data.clear()
    count += 1
    while check not in "SN":
        check = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if check == "N":
        break
print("-=" * 25 + "-")
print(f"No total, você registou {len(people)} pessoas.")
print(f"O maior peso registado foi de {heaviest}Kg. Peso de: ", end="")
for person in people:
    if person[1] == heaviest:
        print(person[0], end=" ")
print()
print(f"O menor peso registado foi de {lightest}Kg. Peso de: ", end="")
for person in people:
    if person[1] == int(lightest):
        print(person[0], end=" ")

""" Resolução Curso em Video """
