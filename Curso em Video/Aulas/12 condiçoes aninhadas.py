'''
if
else

if
elif
...
elif
else
'''

nome = str(input('Qual é o seu nome=: '))
if nome == 'David':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('nome popular')
elif nome in 'Maria Jessica Margarida Vanusa':
    print('que belo nome feminino')

else:
    print('nome normal')