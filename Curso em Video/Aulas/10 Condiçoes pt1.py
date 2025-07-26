# Condições Simples e Compostas

# Algoritmo/Bloco de comandos
"""
carro.siga()
carro.esquerda()
carro.siga()
carro.direita()
carro.siga()
carro.direita()
carro.siga()
carro.esquerda()
carro.siga()
carro.pare()"""

# Condição
""""'''if carro.esquerda():
    true
else:
    false'''
tempo = int(input('Quantos anos tem o  seu carro? '))
'''if tempo <=3:
    print('Carro novo')
else:
    print('Carro Velho')'''
print('carro novo' if tempo <=3 else 'carro velho')
print('Fim'.center(15, '-'))"""
#----------------------------------------------
# Pratica 1
"""
nome = str(input('Qual é o seu nome? '))
if nome == 'David':
    print('Que nome lindo!')
print(f'Bom dia {nome}')
"""
# Pratica 2

n1 = float(input('Escreva a nota do primeiro teste: '))
n2 = float(input('Escreva a nota do segundo teste: '))
m = (n1 + n2) / 2
print(f'As sua media foi de {m:.1f}')
if m >= 6:
    print('Boa nota, continua melhorando essas notas!')
else:
    print('Acho que deverias estudar mais um pouco!')


