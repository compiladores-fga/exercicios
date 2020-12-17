# Estado inicial
q0 = "B"

# Conjunto de estados finais
F = {"C"}

delta = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "b"): "D",
    ("B", "c"): "C",
    ("C", "a"): "B",
    ("D", "b"): "A",
}


def automaton(delta, q0, F, input_string):
    state = q0

    try:
        for c in input_string:
            old = state
            state = delta[state, c]
            print(f"{c}: {old} -> {state}")
    except KeyError:
        state = None
    finally:
        if state in F:
            print('Aceito')
        else:
            print('Rejeitado')


# Exemplo de input válida: caaaaaaabbbaaaac
while True:
    st = input("Entrada: ")
    automaton(delta, q0, F, st)
    if st == '0':
        break
