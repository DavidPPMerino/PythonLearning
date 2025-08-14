""" Enunciado:
Crie um programa que gerencie o aproveitamento de um 'jogador de futebol'.
O programa vai ler o 'nome do jogador' e 'quantas partidas' ele jogou. Depois
vai ler a 'quantidade de gols' feitos em 'cada partida'.
No final, tudo isso será guardado em um 'dicionário', incluido o 'total de gols'
feitos durante o campeonato.
"""

" V1.0 "
player = {}
goals = []
player["nome"] = input("Nome do Jogador: ") 
games = int(input(f"Quantos jogos jogou {player["nome"]}? "))
if games >= 1:
    for i in range(1, (games+1)):
        goals.append(int(input(f"Quantos golos no {i}º jogo? ")))
player["gols"] = goals[:]
player["total"] = sum(goals)
print("-=" * 20 + "-")
print(player)
print("-=" * 20 + "-")
for k, v in player.items():
    print(f"O campo {k} tem o valor {v}.")
print("-=" * 20 + "-")
print(f"O jogador {player['nome']} jogou {len(player['gols'])} jogos.")
for i, v in enumerate(player["gols"]):
    print(f"  → No {i+1}º jogo, fez {f'{v} golos' if v > 1 or v == 0 else f'{v} golo'}.")
print(f"Fez um total de {player["total"]} golos.")
