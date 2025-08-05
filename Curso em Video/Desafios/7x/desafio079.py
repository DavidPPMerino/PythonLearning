""" Enunciado:
Crie um programa onde o usuário possa digitar vários 'valores numéricos' e
cadastre-os em uma 'lista'.
Caso o número já exista lá dentro, ele 'não será adicionado'.
No final, serão exibidos todos os 'valores únicos' digitados, em 'ordem crescente'.
"""
nums = []
check = ""
while True:
    check = ""
    num = int(input("Escreva um valor: "))
    if num in nums:
        print("Valor duplicado! Não vou adicionar...")
    else:
        print("Valor adicionado com sucesso...")
        nums.append(num)
    while check not in ("S", "N"):
        check = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if check == "N":
        break
nums.sort()
print("-=" * 15 + "-")
print(f"Você digitou os valores {nums}")