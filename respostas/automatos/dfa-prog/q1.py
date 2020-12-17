delta = {
    'A':{'b': 'B'},
    'B':{'a': 'B', 'b': 'D','c': 'C'},
    'C':{'a': 'B'},
    'D':{'b': 'A'}
}

def afd(delta, q, accept, text):
    boolean = False
    try:
        for c in text:
            q = delta[q][c]
        return q in accept 
    except:
        return False

text = input()

if afd(delta, 'A', {'D'}, text.lower()):
    print("Aceito")
else:
    print("Rejeitado")
