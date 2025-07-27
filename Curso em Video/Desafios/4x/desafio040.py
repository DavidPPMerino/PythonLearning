""" Enunciado:
        Crie um programa que leia duas notas de um aluno e calcule sua média,
        mostrando uma mensagem no final, de acordo com a média atingida:
        - Média abaixo de 5.0: REPROVADO
        - Média entre 5.0 e 6.9: RECUPERAÇÃO
        - Média 7.0 ou superior: APROVADO
"""

" V1.0 "
# from time import sleep as slp
#
# print('\033[1;31m-'*10,'\033[4;33mCalculadora de Médias\033[m','\033[1;31m-\033[m'*10)
# m1 = float(input('\033[0;33mEscreva a primeira nota: '))
# print('\033[1;31m-'*42)
# m2 = float(input('\033[0;33mEscreva a segunda nota: '))
# print('\033[1;31m-'*42)
# print(f'A analizar a sua média...'.center(42),'\033[m')
# slp(3)
#
# m = (m1 + m2) / 2
# print('\033[1;4;31;43m','Média Calculada'.center(41),'\033[m')
# slp(1)
#
# if m < 5:
#     print(f'Reprovado\nInfelizmente mediante a sua media de {m:.1f} você foi reprovado.')
# elif m >= 7:
#     print(f'Parabéns\nVocê foi aprovado com uma media de {m:.1f}.')
# else: # elif 7 > m >=5:
#     print(f'Recuperação\nDevido a sua média de {m:.1f} será proposto a uma recuperação.')

""" Resolução Curso em Video """
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')