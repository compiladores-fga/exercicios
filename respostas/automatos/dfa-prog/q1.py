# **Q2)** Modifique uma cópia do programa da seção anterior 
# em que o estado inicial seja B e o conjunto de estados de 
# aceite seja {C}.
from functools import partial

estado = 'B'
transicoes = {
    ('A', 'b'): 'B',
    ('B', 'a'): 'B',
    ('B', 'b'): 'D',
    ('B', 'c'): 'C',
    ('C', 'a'): 'B',
    ('D', 'b'): 'A',
}

validos = {'C'}

def DFA(transicoes, estado, validos, st) -> bool:
    for c in st:
        try:
            estado = transicoes[estado, c]
        except KeyError:
            return False
    return estado in validos

abba1 = partial(DFA, transicoes, estado, validos)

if abba1(input('Digite a strig de teste:\n')):
    print('Aceito')
else:
    print('Rejeitado')
