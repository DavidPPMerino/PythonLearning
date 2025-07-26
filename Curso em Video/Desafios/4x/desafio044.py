print('\033[1;31m-'*10,'\033[4;33mCalculadora de metodos de pagamento\033[m','\033[1;31m-\033[m'*10)
#print(f'{' Lojas Guanabara ':=^40}')
val = float(input('\033[33mEscreva o valor: €'))

print('\033[1;31m-'*22,'\033[33mPagamentos\033[m','\033[1;31m-\033[m\033[1;31m\033[m'*23)
print('\033[31m1\033[m \033[33m= \033[32mÀ vista Dinheiro/Cheque'.center(70))
print('\033[31m2\033[m \033[33m= \033[32mÀ vista no Cartão'.center(70))
print('\033[31m3\033[m \033[33m= \033[32m2x no Cartão'.center(70))
print('\033[31m4\033[m \033[33m= \033[32m3x ou mais no Cartão'.center(70))
mtd = int(input('\033[33mEscreva o número do metodo desejado: '))
mtdl = {'1' : 'À vista Dinheiro/Cheque',
        '2' : 'À vista no Cartão',
        '3' : '2x no Cartão',
        '4' : '3x ou mais'}
print('\033[1;31m-'*42)

if mtd == 1:
    print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['1']} \033[33mé de \033[32m€{val-val*10/100:.2f}\033[33mé!')

elif mtd == 2:
    print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['2']} \033[33mé de \033[32m€{val-val*5/100:.2f}\033[33mé!')

elif mtd == 3:
    print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['3']} \033[33mé de \033[32m€{val:.2f}\033[33mé!')

elif mtd == 4:
    print(f'\033[33m O valor atualizado para o metodo de pagamento \033[31m{mtdl['4']} \033[33mé de \033[32m€{val+val*20/100:.2f}\033[33mé!')

else:
    print('Opção invalida!')