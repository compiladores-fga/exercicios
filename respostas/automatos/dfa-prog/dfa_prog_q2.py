Q = {"A", "B", "C", "D"}
Q2 = {"a", "b", "c"}
q0 = "B"
F = {"C"}
Q3 = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "b"): "D",
    ("B", "c"): "C",
    ("C", "a"): "B",
    ("D", "b"): "A",
}


def automato(Q3, q0, F, input_string):
    state = q0

    for c in input_string:
        try:
            state = Q3[state, c]
        except KeyError:
            state = None

    return state in F


inp_str = input("Entrada: ")

if automato(Q3, q0, F, inp_str):
    print("Aceito\n")
else:
    print("Rejeitado\n")
