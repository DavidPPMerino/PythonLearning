""" Enunciado:
        Desenvolva um programa que leia o 'nome', 'idade', e 'sexo' de
        '4 pessoas'. No final do programa, mostre:

        → A 'média de idade' do grupo.   |     → Quantas mulheres têm
        → Qual é o nome do homem         |       'menos de 20' anos.
          'mais velho'.                  |
"""

" V1.0 "
# media_idd = 0
# idd_h = 0
# h_mais_idd = ''
# m_menos20 = 0
# for c in range(1, 5):
#     nome = input('Escreva o seu nome: ').strip()
#     idade = int(input('Escreva a sua idade: '))
#     sexo = input('Qual o seu Sexo? Escreva M/F: ').strip().upper()
#     media_idd += idade
#     if sexo == 'M':
#         if idade > idd_h:
#             idd_h = idade
#             h_mais_idd = nome
#
#     if sexo == 'F':
#         if idade < 20:
#             m_menos20 +=1
# print()
# media_idd /= c
# print(f'''
# A média de idade do grupo é de {media_idd:.0f} anos.
# O nome do homem mais velho é {h_mais_idd.capitalize()}.
# Existem {m_menos20} mulheres com menos de 20 anos.''')

""" Resolução Curso em Video """
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e chama-se {nomevelho}.')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')