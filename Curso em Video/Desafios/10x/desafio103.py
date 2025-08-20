""" Enunciado:
Faça um programa que tenha uma 'função' chamada 'ficha()', que receba dois
'parâmetros opcionais': o 'nome' de um jogador e quantos 'gols' ele marcou.
O programa deverá ser capaz de mostrar a 'ficha do jogador', mesmo que algum
dado não tenha sido informado corretamente.
"""

" V1.0 "
def ficha(n="<desconhecido>", g="0"):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')

nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
if nome == "" and gols == "":
    ficha()
elif nome == "":
    ficha(g=gols)
elif gols == "":
    ficha(n=nome)
else:
    ficha(nome, gols)