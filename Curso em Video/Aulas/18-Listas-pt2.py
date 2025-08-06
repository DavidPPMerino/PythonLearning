dados = ["Pedro", 25]
pessoas = list()
pessoas.append(dados[:])
pessoas.append(["Maria", 19])

pessoas = [["Pedro", 25], ["Maria", 19], ["João", 32]]
#          |   0      1|  |  0      1 |  |  0     1 |
#                  0             1             2

print(pessoas[0][0]) # Escreve Pedro
print(pessoas[1][1]) # Escreve 19
print(pessoas[2][0]) # Escreve João
print(pessoas[1])    # Escreve ['Maria', 19]

