""" Enunciado:
Faça um programa que ajude um jogador da 'MEGA SENA' a criar 'palpites'. O
programa vai perguntar 'quantos jogos' serão gerados e vai sortear '6 números'
'entre 1 e 60' para cada jogo, cadastando tudo em uma 'lista composta'.
"""
from time import sleep
from random import choices
print("--" * 20)
print(f"{"JOGA NA MEGA SENA":^40}")
print("--" * 20)
qty = int(input("Quantos jogos quer que sorteie? "))
print("-=" * 5,f"A sortear {qty} {"jogos" if qty > 1 else "jogo"}".center(20), "=-" * 5)
sleep(2)
for i in range(qty):
    nums = choices(range(1, 61), k=6)
    print(f"Jogo {i+1}: {nums}")
    sleep(1)
print("-=" * 5, "< BOA SORTE >".center(20), "=-" * 5)
print("-=" * 5, "Jogue com moderação".center(20), "=-" * 5)
