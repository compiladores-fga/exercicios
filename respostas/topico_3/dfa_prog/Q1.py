#dfa_prog

Q = {"A", "B", "C", "D"}

Σ = {"a", "b", "c"}

q0 = "A"

F = {"D"}

δ = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "b"): "D",
    ("B", "c"): "C",
    ("C", "a"): "B",
    ("D", "b"): "A",
}


def automato(δ, q0, F, st):
    estado = q0

    for c in st:
        try:
            estado = δ[estado, c]
        except KeyError:
            estado = None

    return estado in F

st = input("Entrada: ")
if(automato(δ, q0, F, st)):
    print("Aceito")
else:
    print("Rejeitado")