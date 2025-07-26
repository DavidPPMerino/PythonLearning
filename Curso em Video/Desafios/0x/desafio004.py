""" Enunciado:
        Faça um programa que leia algo pelo teclado e mostre na tela o seu
        tipo primitivo e todas as informações possíveis sobre ele."""

" V1.0 "
# snbool = {True : 'Sim',False : 'Não'}
# print('======== DESAFIO 004 =======')
# x = input('Escreva algo:')
# print('Informações sobre',x)
# print('O tipo primitivo desse valor é', type(x))
# print('Apenas contem espaços?', snbool[x.isspace()])
# print('É um número?', snbool[x.isnumeric()])
# print('É uma alfabetico?', snbool[x.isalpha()])snbool[]
# print('Está em maiúsculas?', snbool[x.isupper()])
# print('Está em minusculas?', snbool[x.islower()])
# print('Está capitalizado?', snbool[x.istitle()])
# print('É alfanumerico?', snbool[x.isalnum()])
# print('São simbolos?', snbool[x.isascii()])
# print( 'O tipo primitivo é {} apenas contem espaços {}  '.format(type(x), x.isspace()))

""" Resolução Curso em Video """
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiusculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
