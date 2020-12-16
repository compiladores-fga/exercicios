def dfa_teser(dfa_map, initial, final, text):
    valid = False
    state = initial
    try:
        for character in text:
            state = dfa_map[state][character]
        valid = state in final 
    except:
        valid = False
    if valid:
        print("Aceito")
    else: 
        print("Rejeitado")


if __name__ == '__main__':
    dfa_map = {'A':{'b':'B'},
            'B':{'a':'B', 'b': 'D','c':'C'},
            'C':{'a':'B'},
            'D':{'b':'A'}}
    text = input().lower()
    dfa_teser(dfa_map, 'A', {'D'}, text) 