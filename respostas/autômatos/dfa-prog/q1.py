#===============================
# Autômato Determinístico Finito
#===============================

# Conjunto de estados válidos
Q = {"A", "B", "C", "D"}

# Alfabeto de entrada
Σ = {"a", "b", "c"}

# Estado inicial
q0 = "A"

# Conjunto de estados finais
F = {"D"}

# Tabela de transição
δ = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "b"): "D",
    ("B", "c"): "C",
    ("C", "a"): "B",
    ("D", "b"): "A",
}

def automaton(δ, q0, F, input_string):
    state = q0
    for c in input_string:
        try:
            state = δ[state, c]
        except KeyError:
            state = None

    return state in F

st = input("Entrada: ")
if(automaton(δ, q0, F, st)):
    print("Aceito")
else:
    print("Rejeitado")