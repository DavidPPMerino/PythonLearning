# pesos = []
# for c in range(1, 6):
#      peso = float(input(f'Escreva o peso da {c}ª pessoa: Kg '))
#      pesos.append(peso)
# print(f'O maior peso foram {max(pesos):.2f}Kg e o menor foi {min(pesos):.2f}Kg! ')

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Escreva o peso da {p}ª pessoa: Kg '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')