from funcoes import *

def intercalar(a, b, c):
    aux = []
    while not vazia (a):
        push(aux, pop(a))
    aux2 = []
    while not vazia(b):
        push(aux2, pop(b))
    while not vazia(aux):
        v1 = pop(aux)
        v2 = pop(aux2)
        push(a, v1)
        push(b, v2)
        push(c, v1)
        push(c, v2)


p1 = []
p2 = []
p3 = []

push(p1, 1)
push(p1, 2)
push(p1, 3)

push(p2, 4)
push(p2, 5)
push(p2, 6)

intercalar(p1, p2, p3)
mostrar_pilha(p1, 'Pilha 1: ')
mostrar_pilha(p2, '\nPilha 2: ')
mostrar_pilha(p3, '\nPilha 3: ')
