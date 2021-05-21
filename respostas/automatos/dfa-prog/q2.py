# **Q1)** Crie um programa que peça uma string de entrada para o usuário,
# execute o autômato determinístico finito abaixo, verifique se a string
# é aceita ou não pelo autômato e imprima `Aceito` ou `Rejeitado` de acordo 
# com o resultado.
from functools import partial

estado = 'A'
transicoes = {
    ('A', 'b'): 'B',
    ('B', 'a'): 'B',
    ('B', 'b'): 'D',
    ('B', 'c'): 'C',
    ('C', 'a'): 'B',
    ('D', 'b'): 'A',
}

validos = {'D'}

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
