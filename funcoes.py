def push(p, v):
    p.append(v)
    
def pop(p):
    return p.pop()
    
def vazia(p):
    return False if p else True

def mostrar_pilha(p, *args):
    if args: # se a lista de parâmetros tem valores
        print(args[0])
    aux = [] # criar pilha auxiliar
    while not vazia(p): # enquanto a pilha (p) não estiver vazia
        v = pop(p) # retirar o topo
        print(v)
        push(aux, v) # empilha v na pilha auxiliar
    while not vazia(aux):
        push(p, pop(aux))