" V1.0 "
# def leiaDinheiro(msg):
#     check = True
#     while check:
#         v = input(msg).strip().replace(",", ".")
#         for digits in v.split("."):
#             if not digits.isnumeric():
#                 print("\033[31;1mERRO! Digite apenas números!\033[m")
#                 check = True
#                 break
#             else:
#                 check = False
#                 continue
#     return float(v)

""" Resolução Curso em Video """
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m')
        else:
            válido = True
            return float(entrada)
