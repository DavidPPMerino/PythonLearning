""" Enunciado:
Crie uma 'tupla' preenchida com os '20 primeiros' colocados da Tabela do 
'Campeonato Brasileiro de Futebol', na ordem de colocação. Depois mostre:
a) Apenas os '5 primeiros' colocados.
b) Os 'últimos 4' colocados da tabela.
c) Uma lista com os times em 'ordem alfabética'.
d) Em que 'posição' na tabela está o time da 'Chapecoense'
"""
times = ("Coritiba", "Goiás", "Novorizontino", "Chapecoense", "Remo", "Criciúma", "Cuiabá", "Avaí", "Vila Nova", "CRB", "Athletico-PR", "Athletic Club", "Operário-PR", "Atlético-GO", "Ferroviária", "América-MG", "Volta Redonda", "Paysandu", "Amazonas", "Botafogo-SP")
barra = ('-' * 20 + '-')
print(barra)
print(f'Lista de times: {times}')
print(barra)
print(f"Os primeiros 5 colocados: {times[0:5]}")
print(barra)
print(f"Os 4 ultimos são {times[-4:]}")
print(barra)
print(f"Times em ordem algabética: {sorted(times)}")
print(barra)
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição")
print(barra)
print("Fim do programa")