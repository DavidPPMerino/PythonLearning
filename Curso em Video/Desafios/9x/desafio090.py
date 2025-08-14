""" Enunciado:
Faça um  programa que leia 'nome e média' de um aluno guardando também a 
'situação' em um 'dicionário'. 
No final, mostre o conteúdo da estrutura na tela.
7 => aprovado
ex:
nome:
média:
nome é igual a ...
média é igual a ...
situação é igual a ...
"""

" V1.0 "
# student = {}
# student["Nome"] = str(input("Nome: "))
# student["Média"] = float(input(f"Média de {student["Nome"]}: "))
# if student["Média"] >= 7:
#     student["Situação"] = "Aprovado"
# else:
#     student["Situação"] = "Reprovado"
# for k, v in student.items():
#     print(f"{k} é igual a {v}")

""" Resolução Curso em Video """
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.item():
    print(f'{k} é igual a {v}')
