""" Enunciado:
        Crie um programa que leia o nome de uma cidade e diga se ela começa
        ou não com o nome 'SANTO'.
"""

" V1.0 "
# cidade = input('Escreva o nome da sua cidade: ').strip()
# print(f'A sua cidade tem "Santo" no inicio: {cidade.lower().startswith('santo')}')

""" Resolução Curso em Video """
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')