'''
Criar uma função para copiar os dados de uma pilha para outra pilha (mantendo a ordem).
As duas são passadas por parâmetros. No final, mostrar as duas pilhas.
'''

from funcoes import *

def copiar_pilha(po, pd):
    aux = []
    while not vazia(po):
        push(aux, pop(po))
    while not vazia(aux):
        v = pop(aux)
        push(po, v)
        push(pd, v)

p1 = []
push(p1, 10)
push(p1, 20)
push(p1, 30)
p2 = []
copiar_pilha(p1, p2)
mostrar_pilha(p1, 'Pilha 1: ')
mostrar_pilha(p2, '\nPilha 2: ')