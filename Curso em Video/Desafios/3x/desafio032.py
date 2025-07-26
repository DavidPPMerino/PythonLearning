ano = int(input('Que ano quer confirmar se é Bissexto? Escreva 0 para analisar o ano atual: '))
'''if str(ano).endswith('00'):
    if ano % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')
else:
    if ano % 4 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')'''
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')