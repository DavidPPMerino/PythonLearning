pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas)          # Escreve {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas['nome'])  # Escreve Gustavo
# print(f'O {pessoas["nome"]} tem {pessoas['idade']} anos.')  # Antigamente era necessario usar aspas diferentes 
#                                                             # atualmente ja se pode usar as mesmas.
# print(pessoas.keys())       # Escreve dict_keys(['nome', 'sexo', 'idade'])
# print(pessoas.values())     # Escreve dict_values(['Gustavo', 'M', 22])
# print(pessoas.items())      # Escreve dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

# for k in pessoas.keys():        # Escreve:
#     print(k)                    # nome
#                                 # sexo
#                                 # idade

# for k in pessoas.values():      # Escreve:
#     print(k)                    # Gustavo
#                                 # M
#                                 # 22
                    
# for k, v in pessoas.items():    # Escreve:
#     print(f'{k} = {v}')         # nome = Gustavo
#                                 # sexo = M
#                                 # idade = 22

# pessoas['peso'] = 98.5          # é possivel adicionar diretamente ou modificar

""" Dicionario dentro de lista """
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)            # Adiciona o dicionário estado1 à lista
# brasil.append(estado2)            # Adiciona o dicionário estado2 à lista
# print(estado1)                    # Escreve o dicionário estado1
# print(estado2)                    # Escreve o dicionário estado2
# print(brasil)                     # Escreve a lista que tem os dois estados
# print(brasil[0])                  # Escreve o dicionário na posição 0(estado1)
# print(brasil[0]['uf'])            # Escreve Rio de Janeiro

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())      # No dicionário nao se pode usar [:] tem de ser .copy()
for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()