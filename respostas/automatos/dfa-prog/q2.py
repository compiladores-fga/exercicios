test = {
    'A':{'b': 'B'},
    'B':{'a': 'B', 'b': 'D','c': 'C'},
    'C':{'a': 'B'},
    'D':{'b': 'A'}
}

def afd(test, q, accept, text):
    try:
        for c in text:
            q = test[q][c]
        return q in accept 
    except:
        return False

text = input()

if afd(test, 'B', {'C'}, text.lower()):
    print("Aceito")
else:
    print("Rejeitado")