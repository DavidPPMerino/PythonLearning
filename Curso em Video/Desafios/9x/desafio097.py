""" Enunciado:
Faça um programa que tenha uma 'função' chamada 'escreva()', que receba um 
texto qualquer como 'parâmetro' e mostre uma mensagem com tamanho adaptável-
EX:
escreva('Olá, Mundo!')
SAIDA:
~~~~~~~~~~~~~
 Olá, Mundo! 
~~~~~~~~~~~~~
"""

" V1.0 "
# def escreva(txt):
#     print('~' * (len(txt) + 4))
#     print(txt.center(len(txt) + 4))
#     print('~' * (len(txt) + 4))


# #Programa
# escreva('Olá, Mundo')
# escreva('Curso de Python no Youtube')
# escreva('CeV')

""" Resolução Curso em Video """
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')