""" Enunciado:
Crie um programa onde '4 jogadores' joguem um 'dado' e tenham resultados
'aleatórios'. Guarde esses resultados em um 'dicionário'. 
No final, coloque esse dicionário em 'ordem' sabendo que o 'vencedor' tirou o 
'maior número' no dado.
"""

" V1.0 "
from random import randint
from time import sleep
jogadores ={}
print("Valores sorteados:")
sleep(1)
for i in range(1, 5):
    jogadores[f"Jogador{i}"] = randint(1, 6)
for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
    sleep(1)
print("Ranking dos jogadores:")
sorted_jogadores = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
sleep(1)
for i, (k, v) in enumerate(sorted_jogadores.items()):
    print(f"{i+1}º Lugar: {k} com {v}")
    sleep(1)
