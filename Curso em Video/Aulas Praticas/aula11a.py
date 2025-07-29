print("'\033[1;31;45mOlá, Mundo!\033[m':", '\033[1;31;45mOlá, Mundo!\033[m')
print('\033[2;31m-'*15)

# dicionario
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'peb' : '\033[7;30m',
         'vermelho' : '\033[31m'}
print(f"{cores['peb']}Boa noite{cores['limpa']},{cores['vermelho']}Mundo{cores['limpa']}!!!")