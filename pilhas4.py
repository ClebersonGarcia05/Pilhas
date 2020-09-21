from funcoes import * 

def tirar_base(p):
    aux = []
    while not vazia(p):
        push(aux, pop(p))
    pop(aux)
    while not vazia(aux):
        push(p, pop(aux))

p1 = []
push(p1, 10)
push(p1, 20)
push(p1, 30)
mostrar_pilha(p1, 'Pilha antes de tirar a base: ')
tirar_base(p1)
mostrar_pilha(p1, '\nPilha depois de tirar a base: ')