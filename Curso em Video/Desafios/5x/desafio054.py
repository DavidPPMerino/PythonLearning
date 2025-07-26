from datetime import date


cur_year = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = cur_year - ano

    if idade >= 18:
    # if cur_year - ano >= 18:
        maior += 1

    else:
        menor += 1

if maior == c:
    print(f'Todas as {maior} pessoas atingiram a maioridade!')
elif menor == c:
    print(f'Nenhuma das {menor} pessoas atingiu a maioridade')
else:
    print(f'{maior} pessoas já atingiram a maioridade e {menor} ainda nao atingiram!')