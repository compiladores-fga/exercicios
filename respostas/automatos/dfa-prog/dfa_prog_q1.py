Q = {"A", "B", "C", "D"}
Q2 = {"a", "b", "c"}
q0 = "A"
F = {"D"}
Q3 = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "b"): "D",
    ("B", "c"): "C",
    ("C", "a"): "B",
    ("D", "b"): "A",
}


def automato(Q3, q0, F):
    state = q0

    for c in inp_str:
        try:
            state = Q3[state, c]
        except KeyError:
            state = None

    return state in F


inp_str = input("Entrada: ")

if automato(Q3, q0, F):
    print("Aceito\n")
else:
    print("Rejeitado\n")
