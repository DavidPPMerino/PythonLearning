""" Enunciado:
        Elabora um programa que calcule o valor a ser pago por um produto,
        considerando o seu 'preço normal' e 'condição de pagamento':
        - À vista dinheiro/cheque: 10% de desconto
        - À vista no cartão: 5% de desconto
        - Em até 2x no cartão: preço normal
        - 3x ou mais no cartão: 20% de juros
"""

" V1.0 "
# print('\033[1;31m-'*10,'\033[4;33mCalculadora de metodos de pagamento\033[m','\033[1;31m-\033[m'*10)
# val = float(input('\033[33mEscreva o valor: €'))
#
# print('\033[1;31m-'*22,'\033[33mPagamentos\033[m','\033[1;31m-\033[m\033[1;31m\033[m'*23)
# print('\033[31m1\033[m \033[33m= \033[32mÀ vista Dinheiro/Cheque'.center(70))
# print('\033[31m2\033[m \033[33m= \033[32mÀ vista no Cartão'.center(70))
# print('\033[31m3\033[m \033[33m= \033[32m2x no Cartão'.center(70))
# print('\033[31m4\033[m \033[33m= \033[32m3x ou mais no Cartão'.center(70))
# mtd = int(input('\033[33mEscreva o número do metodo desejado: '))
# mtdl = {'1' : 'À vista Dinheiro/Cheque',
#         '2' : 'À vista no Cartão',
#         '3' : '2x no Cartão',
#         '4' : '3x ou mais'}
# print('\033[1;31m-'*42)
#
# if mtd == 1:
#     print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['1']} \033[33mé de \033[32m€{val-val*10/100:.2f}\033[33mé!')
#
# elif mtd == 2:
#     print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['2']} \033[33mé de \033[32m€{val-val*5/100:.2f}\033[33mé!')
#
# elif mtd == 3:
#     print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['3']} \033[33mé de \033[32m€{val:.2f}\033[33mé!')
#
# elif mtd == 4:
#     print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['4']} \033[33mé de \033[32m€{val+val*20/100:.2f}\033[33mé!')
#
# else:
#     print('Opção invalida!')

""" Resolução Curso em Video """
print(f'{" LOJAS GUANABARA ":=^40}')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc} de R${parcela:.2f} COM JUROS')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
