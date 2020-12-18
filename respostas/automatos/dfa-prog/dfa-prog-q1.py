def dfa_prog(delta, initial, final, input_string):
    accepted = False
    state = initial
    try:
        for char in input_string:
            state = delta[state][char] 
        
        accepted = state in final
    
    except:
        accepted = False
    
    if accepted:
        print("Aceito")
    else: 
        print("Rejeitado")


dfa = {
    'A': {'b':'B'},
    'B': {'a':'B', 'c':'C', 'b':'D'},
    'C': {'a':'B'},
    'D': {'b':'A'}
}

input_string = input()

# Exemplos
# baacab - Aceito
# bb - Aceito
# abb - Rejeitado
# baca - Rejeitado

dfa_prog(dfa, 'A', {'D'}, input_string)
