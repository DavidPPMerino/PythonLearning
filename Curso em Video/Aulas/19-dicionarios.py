####### Dicionários #######

# tuplas ()
# listas []
# dicionarios {}

# dados = dict()
# dados{'nome': 'Pedro', 'idade':25}
# print(dados['nome']) # Escreve Pedro
# print(dados['idade']) # Escreve 25
# dados['sexo'] = 'M'
# del dados['idade']

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas',
        }
print(filme.values())   # Escreve Star Wars', 1977, George Lucas'
print(filme.keys())      # Escreve titulo, ano, diretor
print(filme.items())      # Escreve ambos

for k,v in filme.items():
    print(f'O {k} é {v}')   # Escreve:
                            # O titulo é Star Wars
                            # O ano é 1977
                            # O diretor é George Lucas
