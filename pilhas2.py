from funcoes import *

def qtde_pilha(p):
    qe = 0
    aux = []
    while not vazia(p):
        qe += 1
        push(aux, pop(p))
    while not vazia(aux):
        push(p, pop(aux))
    return qe

import random as rd

p2 = []
for x in range(rd.randint(0, 10)):
    push(p2, x)
mostrar_pilha(p2, 'Pilha 2:')
q = qtde_pilha(p2)
print(f'\nQtde de elementos = {q}')