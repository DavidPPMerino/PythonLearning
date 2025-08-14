""" Enunciado:
Crie um programa que leia 'nome', 'sexo' e 'idade' de 'várias pessoas', 
guardando os dados de cada pessoa em um 'dicionário' e todos os dicionários em 
uma 'lista'. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) A 'média' da idade do grupo.
c) Uma lista com todas as 'mulheres'.
d) uma lista com todas as pessoas com 'idade' acima da 'média'.
"""

" V1.0 "
people = []
person = {}
while True:
    person["nome"] = input("Nome: ").strip()
    while True:
        person["sexo"] = input("Sexo: [M/F] ").upper().strip()
        if person["sexo"] in "MF":
            break
    person["idade"] = int(input("Idade: "))
    people.append(person.copy())
    while True:
        check = input("Quer continuar? [S/N] ").upper().strip()
        if check in "SN":
            break
    if check in "N":
        break
print("-=" * 20 + "-")
print(f"→ O grupo tem {len(people)} pessoas.")
average = 0
for p in people:
    average += int(p["idade"]) / len(people)
print(f"→ A média de idade é de {average:.0f} anos.")
print("→ As mulheres registadas foram: ", end=" ")
for p in people:
    if p["sexo"] in "Ff":
        print(p["nome"], end=" ")
print()
print("→ Lista das pessoas acima da média: ")
for p in people:
    print()
    if p["idade"] > average:
        for k, v in p.items():
            print(f"{k} = {v};", end=" ")
print("<< Programa terminado >>")