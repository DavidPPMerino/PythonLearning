""" Enunciado:
        Crie um programa que leia vários números inteiros pelo teclado.
        O programa só vai parar quando o usuário digitar o valor 999, que é a
        condição de parada.
        No final, mostra quantos números foram digitados e qual foi a soma
        entre eles (desconsiderando a flag).
"""

" V1.0 "
# num = 0
# soma = 0
# count = 0
# while num != 999:
#     num = int(input('''Escreva um número inteiro,
#     se desejar parar escreva 999: '''))
#     if num == 999:
#         print('A analisar os dados inseridos')
#     else:
#         soma += num
#         count += 1
#         print('Valor adicionado.')
# print(f'Você introduziu {count} valores e a soma deles é {soma}.')

""" Resolução Curso em Video """

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')