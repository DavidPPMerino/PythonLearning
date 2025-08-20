""" Enunciado:
Faça um programa que tenha uma 'função' 'notas()' que pode receber várias 
notas de alunos e vai retornar um 'dicionário' com as seguintes informações:
→ Quantidade de notas
→ A maior nota
→ A menor nota
→ A média da turma
→ A situação (opcional)

Adiciona também as 'docstrings' da função.
"""

" V1.0 "
# def notas(*num, sit=False):
#     """
#     -> Função para analisar notas e situações de uma turma.
#     :param num: uma ou mais notas dos alunos (Aceita várias notas)
#     :param sit: Indica se deve ou não adicionar a situação (Opcional)
#     :return: Dicionário com várias informações sobre a situação da turma.
#     """
#     valores = dict()
#     for i,n in enumerate(num):
#         if i == 0:
#             valores["total"] = 0
#             valores["maior"] = n
#             valores["menor"] = n
#             valores["media"] = 0
#         else:
#             if n < valores["menor"]:
#                 valores["menor"] = n
#             if n > valores["maior"]:
#                 valores["maior"] = n
#         valores["total"] += 1
#         valores["media"] += n
#     valores["media"] /= len(num)
#     if sit:
#         if valores["media"] >= 7:
#             valores["situação"] = "BOA"
#         elif valores["media"] <= 5:
#             valores["situação"] = "RUIM"
#         elif 7 > valores["media"] > 5:
#             valores["situação"] = "RAZOÁVEL"
#     return valores

# # Programa Principal
# resp = notas(5.5, 9.5, 10, 6.5, sit=True)
# resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
# print(resp)

""" Resolução Curso em Video """
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (Aceita várias)
    :param sit: valor opcional,indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)