""" Enunciado:
Aprimore o 'Desafio 093' para que ele funcione com 'vários jogadores', incluindo
um sistema de visualização de 'detalhes do aproveitamento' de cada jogador."""

" V1.0 "
players = []
player = {}
goals = []
while True:
    print("-" * 40)
    player["nome"] = input("Nome do Jogador: ").strip()
    games = int(input(f"Quantos jogos jogou {player["nome"]}? "))
    if games >= 1:
        for i in range(1, (games+1)):
            goals.append(int(input(f"Quantos golos no {i}º jogo? ")))
    player["gols"] = goals[:]
    player["total"] = sum(goals)
    players.append(player.copy())
    goals.clear()
    while True:
        check = input("Quer continuar? [S/N] ").strip().upper()
        if check in "SN":
            break
    if check in "N":
        break
print("-=" * 25 + "-")
print(f"{" Cod"} | {"Nome":^15} | {"Golos":^15} | {"Total":^7}")
print("-" * 51)
for i, p in enumerate(players):
    print(f"{i+1:^4} | {p["nome"]:^15} | {str(p["gols"]):^15} | {p["total"]:^7}")
print("-=" * 25 + "-")
while True:
    check2 = int(input("Mostrar dados de qual jogador? (999 para terminar) ")) - 1
    if check2 == 998:
        print(">>- Volte sempre -<<".center(51))
        break
    elif check2 <= (len(players) - 1):
        print(f"-- Levantamento do jogador {players[check2]["nome"]}:")
        for i, v in enumerate(players[check2]["gols"]):
            print(f"  → No {i+1}º jogo, fez {f'{v} golos' if v > 1 or v == 0 else f'{v} golo'}.")
        print("-" * 51)
    else:
        print(f"ERRO! Não existe jogador com o código {check2 + 1}! Tente novamente")
        print("-" * 51)
