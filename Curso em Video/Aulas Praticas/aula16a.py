# lanche = "Hambúrguer", "Suco", "Pizza", "Pudim"
# print(f"lanche = {lanche}")
# print(f"lanche[1] = {lanche[1]}")
# print(f"lanche[1:3] = {lanche[1:3]}")
# print(f"lanche[2:] = {lanche[2:]}")
# print(f"lanche[:2] = {lanche[:2]}")
# print("lanche[1] = 'refrigerante'")
# print("print(lanche[1]) = TypeError: 'tuple' object does not support item assignment") 

# print("""for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')""")
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

# print(f"print(len(lanche)) = {len(lanche)}")

# print("""for cont in range(0, len(lanche)):
#     print(lanche[cont])
#     print(cont)""")
# for cont in range(0, len(lanche)):
#     print(lanche[cont])
#     print(cont)

# print("""for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')""")
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print(f"print(sorted(lanche)) = {sorted(lanche)}")


# a = (2, 5, 4) 
# b = (5, 8, 1, 2)
# c = a + b # junta a tupla a e a b dando o resultado de 2, 5, 4, 5, 8, 1, 2
# c = b + a # junta a tupla a e a b dando o resultado de 5, 8, 1, 2, 2, 5, 4
# print(c.count(5)) # conta quantos 5 tem na tupla c
# print(c)
# print(c.index(5)) # mostra a primeira posição do 5
# print(c.index(5, 1)) # mostra a primeira posição do cinco depois de 1

pessoa = ("Gustavo", 39, "M", 99.88)
del(pessoa) # apaga a tupla
