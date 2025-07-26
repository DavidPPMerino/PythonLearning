""" Enunciado:
        Crie um programa que leia 'vários números' inteiros pelo teclado.
        No final da execução, mostra a 'média entre todos' os valores e qual
         foi o 'maior' e o 'menor' valor lido. O programa deve perguntar ao
         usuário se ele quer ou não 'continuar' a digitar valores.
"""

" V1.0 "
# continuar = 1
# media = 0
# count = 0
# maior = 0
# menor = 0
# while continuar == 1:
#     num = int(input('Escreva um numero inteiro: '))
#     count += 1
#     media += num
#     if count == 1:
#         maior = num
#         menor = num
#     else:
#         if num > maior:
#             maior = num
#         elif num < menor:
#             menor = num
#     verificar = 0
#     while verificar not in (1,2):
#         continuar = int(input('''[ 1 ] Sim\n[ 2 ] Não
#         Deseja continuar? '''))
#         if continuar in (1,2):
#             verificar = continuar
#             if continuar != 1:
#                 print(f'''Foram introduzidos {count} valores média deles foi de {media/count:.2f}
#                  O maior número introduzido foi {maior}
#                  O menor número introduzido foi {menor}''')
#         else:
#             print('Opção Inválida!')
#
#

""" Resolução Curso em Video """

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')