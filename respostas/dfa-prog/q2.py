
dfa = {'A':{'b':'B',},
       'B':{'a':'B', 'b': 'D','c': 'C'},
       'C':{'a':'B'},
       'D':{'b': 'A'}}

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
      try:
        state = transitions[state][c]
      except:
        return('Rejeitado')
    if(state in accepting):
      return('Aceito')
    else:
      return('Rejeitado')

user_input = input("Digite a sequencia entradas ex:'bbb': ")

print(accepts(dfa,'B','C',user_input))