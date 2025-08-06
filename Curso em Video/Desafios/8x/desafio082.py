""" Enunciado:
Crie um programa que vai ler 'vários números' e colocar em uma 'lista'.
Depois disso, crie 'duas listas extras' que vão contar apenas os valores 'pares'
e os valores 'ímpares' digitados, respetivamente.
Ao final, mostre o conteúdo das 'três listas' geradas.
"""

nums = []
while True:
    nums.append(int(input("Escreva um valor: ")))
    check = " "
    while check not in "SN":
        check = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if check == "N":
        break
evens = []
odds = []
for num in nums:
    if num % 2:
        odds.append(num)
    else:
        evens.append(num)
print("-=" * 15 + "-")
print(f"A lista completa é {nums}")
print(f"A lista de pares é {evens}")
print(f"A lista de ímpares é {odds}")


