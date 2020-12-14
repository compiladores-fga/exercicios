def dfa_prog(delta, initial, accepting, text):
    boolean = False
    state = initial
    try:
        for c in text:
            state = delta[state][c]
        boolean = state in accepting 
    except:
        boolean = False
    if boolean:
        print("Aceito")
    else: 
        print("Rejeitado")

dfa_map = {
    'A':{'b': 'B'},
    'B':{'a': 'B', 'b': 'D','c': 'C'},
    'C':{'a': 'B'},
    'D':{'b': 'A'}
}

dfa_prog(dfa_map, 'A', {'D'}, input().lower())
