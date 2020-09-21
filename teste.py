from funcoes import push, pop

pilha = []
push(pilha, 10)
push(pilha, 20)
push(pilha, 30)
val = pop(pilha)
print(f'{val} desempilhado...')
push(pilha, 40)
print(pilha)
