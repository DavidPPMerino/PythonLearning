""" Erros e Exceções e seus tratamentos """

# primt(x)      # Erro de sintaxe não é este erro que vamos tratar

#--------------#
# print(x)        # Erro semantico (NameError) Variavel x não existe
# Na realidade chamasse exceção NameError
#--------------#
# n = int(input('Num')) # Se Escrevermos um número por extenso da outra exceção
# Exceção ValueError porque deveria receber um numero inteiro e recebeu string
#--------------#
a=5
b=0
r = a / b 
# Exceção ZeroDivisionError divisão por zero não pode acontecer
#--------------#
r = 2 / '2' 
# Exceção TypeError por conta do segundo 2 ser uma string no python não é possivel
#--------------#
lst = [3,6,4]
print(lst[3])
# Exceção IndexError ou KeyError no caso dos dicionários
#--------------#
import uteis # Não existe
# Exceção ModuleNotFoundError 


### Existem imensas exceções e não é preciso sabe-las de cor

""" Tratamento de exceções """
try:
    # Operaçãp
except:
    # Falhou
else:                   #Opcional
    # Deu certo
finally:
    # Certo / Falha     #Opcional mas vai rodar sempre
#------------------------#
except Exception as erro:   # cria uma variavel com o erro


# Um 'try' pode ter varios 'except'