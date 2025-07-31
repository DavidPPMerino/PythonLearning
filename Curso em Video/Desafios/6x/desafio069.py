""" Enunciado:
        Crie um programa que leia a 'idade' e o 'sexo' de 'várias pessoas'.
        A cada pessoa cadastrada, o programa deverá perguntar se o 'usuário'
        quer ou não continuar. No final, mostre:
        a) quantas pessoas tem mais de 18 anos.
        b) quantos homens foram cadastrados.
        c) quantas mulheres tem menos de 20 anos.
"""

" V1.0 "
# older_18 = 0
# men_amount = 0
# woman_less20 = 0
# while True:
#     gender = ' '
#     continue = ''
#     print('-' * 30)
#     print('REGISTE UMA PESSOA'.center(30))
#     print('-' * 30)
#     age = int(input('Idade: '))
#     while gender not in ['M', 'F']:
#         gender = str(input('Sexo: [ M / F ] ')).strip().upper()
#     if age > 18:
#         older_18 += 1
#     if gender == 'M':
#         men_amount += 1
#     if gender == 'F' and age < 20:
#         woman_less20 += 1
#     print('-' * 30)
#     while continue not in ['S', 'N']:
#         continue = str(input('Quer continuar? [S/N] ')).strip().upper()
#     if continue == 'N':
#         break
# print('-' * 30)
# print(f'{'Estatísticas Finais':=^30}')
# print(f'Total de pessoas com mais de 18 anos: {older_18}')
# print(f'Ao todo temos {'nenhum' if men_amount == 0 else men_amount} {'homem registado' if men_amount <= 1 else 'homens registados'}')
# print(f'E temos {woman_less20} {'mulher' if woman_less20 == 1 else 'mulheres'} com menos de 20 anos')

""" Resolução Curso em Video """
tot18 = totH = totM20 =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')