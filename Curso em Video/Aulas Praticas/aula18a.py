# teste = list()
# teste.append("Gustavo")
# teste.append(40)
# galera = list()
# galera.append(teste[:]) # se nao usar [:] cria uma ligação ao teste em vez de copiar
# teste[0] = "Maria"
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# for p in galera:
#     print(p)        # Escreve os dados de cada pessoa
#     print(p[0])     # Escreve o nome de cada pessoa
#     print(p[1])     # Escreve a idade de cada pessoa

# galera = list()
# dado = list()
# for c in range(0, 3):
#     dado.append(str(input("Nome: ")))
#     dado.append(int(input("Idade: ")))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade.")
