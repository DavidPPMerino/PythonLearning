frase = 'Curso em Video Python'
print(frase)
print('012345678911111111112')
print('          01234567890')
print('-'*5,'Fatiamento', '-'*5)
#fatiamento
''' Fatiamento de um digito'''
print('frase[9]: ', frase[9])
''' Fatiamento de uma palavra
9:14 começa no 9 e imprime só até ao 13'''
print('frase[9:14]: ', frase[9:14])
''' Fatiamento alternado'''
print('frase[9:21:22]: ', frase[9:21:2])
''' Fatiamento desde o inicio'''
print('frase[:5]: ', frase[:5])
''' Fatiamento até ao final'''
print('frase[15:]: ', frase[15:])
''' Fatiamento alternado até ao final'''
print('frase[9::3]: ', frase[9::3])
print('-'*5, 'Análise', '-'*5)
#Análise
''' comprimento'''
print('len(frase): ', len(frase))
''' Contar x'''
print('frase.count("o"): ', frase.count('o'))
''' Contar x com fatiamento'''
print('frase.count("o", 0, 13): ', frase.count('o',0,13))
''' Encontrar'''
print('frase.find("deo"): ', frase.find('deo'))
''' se nao encontrar retorna -1'''
print('frase.find("Android"): ', frase.find('Android'))
''' Verificar'''
print('"Curso" in frase: ', 'Curso' in frase)
print('-'*5,'Transformação', '-'*5)
#Transformação
''' Substituir'''
print('frase.replace("Python","Android"): ', frase.replace('Python','Android'))
'''Tornar Maiusculas'''
print('frase.upper(): ', frase.upper())
''' Tornar Minusculas'''
print('frase.lower(): ', frase.lower())
'''Capitalização 1 digito da string maiusculo'''
print('frase.capitalize(): ', frase.capitalize())
''' Titulo 1 digito de cada palavra maiusculo'''
print('frase.title(): ', frase.title())
print('')

print('-'*5,'Frase 2', '-'*5)
frase2 = '   Aprenda Python  '
print(frase2)
print('0123456789111111111')
print('          012345678')
''' Remover espaços no inicio e final'''
print('frase2.strip(): ', frase2.strip())
'''Remover espaços da direita'''
print('frase2.rstrip(): ', frase2.rstrip())
''' Remover espaços da esquerda'''
print('frase2.lstrip(): ', frase2.lstrip())

#divisão
print('-'*5, 'Divisão', '-'*5)
print(frase)
print('012345678911111111112')
print('          01234567890')
'''Dividir strings'''
print('frase.split(): ', frase.split())
print('-'*5, 'Obter item de lista', '-'*5)
print('split = frase.split()')
split = frase.split()
print('split[0]: ', split[0])
print('-'*5, 'Fatiamento de item da lista', '-'*5)
print('split[2][3]: ', split[2][3])

#junção
print('-'*5, 'Junção', '-'*5)
print('split = frase.split()')
split = frase.split()
print('"-".join(frase): ', '-'.join(split))
print('--ou--')
print('"-".join(frase.split()): ', '-'.join(frase.split()))

'''print varias linhas'''
print("""blablabala
blalalja blalaal
balalala""")