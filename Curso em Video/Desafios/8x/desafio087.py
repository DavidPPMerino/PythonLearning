""" Enunciado:
Aprimore o 'desafio anterior', mostrando no final:
a) A 'soma' de todos os 'valores pares' digitados.
b) a 'soma' dos valores da 'terceira coluna'.
c) o 'maior' valor da 'segunda linha'.
"""

matrix = [[], [], []]
evensum = thirdsum = highest = 0
for col, line in enumerate(matrix):
    for i in range(0, 3):
        num = int(input(f"Escreva um valor para [{col}, {i}]: "))
        matrix[col].insert(i, num)
print("-=" * 20 + "-")
for i, line in enumerate(matrix):
    for col, num in enumerate(line):
        print(f"[ {num} ]", end="")
        if not num % 2:
            evensum += num
        if col == 2:
            thirdsum += num
        if i == 1 and num > highest:
            highest = num
    print()
print("-=" * 20 + "-")
print(f"A soma dos valores pares é {evensum}.")
print(f"A soma dos valores da terceira coluna é {thirdsum}.")
print(f"O maior valor da segunda linha é {highest}.")

