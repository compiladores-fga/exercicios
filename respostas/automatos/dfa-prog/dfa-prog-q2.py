
Q = {"A", "B", "C", "D"}

sig = {"a", "b", "c"}

q0 = "B"

lista = {"C"}

dt = {
  ("A", "b"): "B",
  ("B", "a"): "B",
  ("B", "b"): "D",
  ("B", "c"): "C",
  ("C", "a"): "B",
  ("D", "b"): "A",
}


def automato(input_string, dt, q0, lista):
  state = q0
  
  for i in input_string:
    try:
      state = dt[state, i]
    except KeyError:
      state = None
    
    return state in lista


input_string = input("Entrada: ")

if(automato(input_string, dt, q0, lista)):
  print("Aceito\n")
else:
  print("Rejeitado\n")


