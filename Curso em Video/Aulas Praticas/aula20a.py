def soma(a, b): #"a" e "b" são parametros
    x = a + b
    print(x)


# Programa Principal
soma(4, 5)
a = 4 
b = 5
s = a + b
print(s)

soma(8, 9)
a = 8 
b = 9
s = a + b
print(s)

soma(2, 1)
a = 2 
b = 1
s = a + b
print(s)

soma(4) # da erro por falta de parametros

soma(a=4, b=5)
soma(b=4, a=5) # é possivel inverter os parametros mas é preciso explicitar ambos

"Empacotar parametros"
def contador(* núm): #desempacota núm e cria uma tupla
    print(núm)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(* núm): #desempacota núm e cria uma tupla
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')

" Função com listas "
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]


" Desempacotamento"
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')