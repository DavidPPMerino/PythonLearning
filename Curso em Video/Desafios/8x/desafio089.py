""" Enunciado:
Crie um programa que leia 'nome' e 'duas notas' de vários alunos e guarde tudo
em uma 'lista composta'. No final, mostre um 'boletim' contendo a 'média' de 
cada um e permita que o usuário possa mostrar as 'notas' de cada aluno 
individualmente.
"""

students = []
while True:
    check = " "
    name = str(input("Nome: "))
    note1 = float(input("Nota 1: "))
    note2 = float(input("Nota 2: "))
    students.append([name, [note1, note2]])
    while check not in "SN":
        check = input("Quer continuar? [S/N] ").upper().strip()[0]
    print("-=" * 25 + "-")
    if check == "N":
        break
print("No. |","Nome".center(18),"|", "Média".center(10))
print("-" * 37)
for i, student in enumerate(students):
    print(f"{i:<4}", end="|")
    print(f" {student[0]:^19}", end="|")
    print(f" {(student[1][0] + student[1][1]) / 2:^10.1f}")
check2 = 0
while check2 != 999:
    print("-=" * 25 + "-")
    check2 = int(input("Quer ver as notas de qual aluno? (999 interrompe): "))
    if check2 == 999:
        break
    print(f"As notas de {students[check2][0]} são {students[check2][1]}".center(51))
print(" A terminar o programa ".center(51, "-"))
print(" Volte sempre ".center(51, "-"))

