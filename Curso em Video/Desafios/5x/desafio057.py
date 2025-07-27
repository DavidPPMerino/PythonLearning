""" Enunciado:
        Faça um programa que leia o sexo de uma pessoa, mas só aceite os
        valores 'M' ou 'F'.
        Caso esteja errado, peça a digitação novamente até ter um
        valor correto.
"""

" V1.0 "
# sexo = ' '
# tentativas = 0
# while sexo not in ('M', 'F'):
#     sexo = input('Sexo: [M/F] ').strip().upper()
#     if sexo not in ('M', 'F'):
#         print('Opção invalida!')
#         tentativas += 1
# print(f'Precisou de {tentativas} tentativas para escolher o seu sexo.')

""" Resolução Curso em Video """
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registado com sucesso!')