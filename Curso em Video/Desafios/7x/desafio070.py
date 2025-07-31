""" Enunciado:
        Crie um programa que leia o 'nome' e o 'preço' de 'vários produtos'.
        O programa deverá perguntar se o 'usuário' vai continuar.
        No final, mostre:
        a) Qual é o 'total gasto' na compra.
        b) Quantos produtos custam 'mais' de 'R$1000'.
        c) Qual é o 'nome' do produto mais 'barato'.
"""

" V1.0 "
# print('-=' * 20 + '-')
# print(f'{'LOJA SUPER BARATÃO':^41}')
# print('-=' * 20 + '-')
# amount_sum = 0
# more1000_items = 0
# cheap_name = ' '
# cheap_price = 0
# count = 0
# while True:
#     name = input('Nome do produto: ').strip()
#     price = float(input('Preço: R$ '))
#     count += 1
#     amount_sum += price
#     if price > 1000:
#         more1000_items += 1
#     if count == 1:
#         cheap_name = name
#         cheap_price = price
#     if price < cheap_price:
#         cheap_name = name
#         cheap_price = price

#     while True:
#         check = str(input('Deseja continuar? [S/N] ')).strip().upper()
#         if check in ('N', 'S'):
#             break
#     if check == 'N':
#         print('FIM DO PROGRAMA'.center(40, '='))
#         break
# print(f'Você comprou {count} artigos e o total é de R${amount_sum}')
# print(f'Comprou {more1000_items} produtos que custam mais que R$1000')
# print(f'O produto mais barato foi {cheap_name} que custa R${cheap_price}')

""" Resolução Curso em Video """
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar= [S/N] ')).strip().upper()[0]
    if resp =='N':
        break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
