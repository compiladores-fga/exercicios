from functools import partial

estado = 2
transicoes = {
    (1, "b"): 2,
    (2, "a"): 2,
    (2, "c"): 3,
    (2, "b"): 4,
    (3, "a"): 2,
    (4, "b"): 1
}

validos = {3}

def DFA(transicoes, estado, validos, st) -> bool:
    for c in st:
        try:
            estado = transicoes[estado, c]
        except KeyError:
            return False
    return estado in validos

entrada = input()

res = DFA(transicoes, estado, validos, entrada)

if(res):
    print("Aceito")
else:
    print("Rejeitado")