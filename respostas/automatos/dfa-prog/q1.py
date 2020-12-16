#q1 dfa-prog
q = {"A", "B", "C", "D"}

simga = {"a", "b", "c"}

q0 = "A"

list = {"D"}

delta = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "b"): "D",
    ("B", "c"): "C",
    ("C", "a"): "B",
    ("D", "b"): "A",
}


def automato(str_in, delta, q0, list):
    state = q0

    for component in str_in:
        try:
            state = delta[state, component]
        except KeyError:
            state = None
    return state in list

str_in = input("Entrada: ")
if(automato(str_in, delta, q0, list)):
    print("Aceito")
else:
    print("Rejeitado")