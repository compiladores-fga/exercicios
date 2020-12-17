import sys

STATES = {'A', 'B', 'C', 'D'}
INITIAL_STATE = 'B'
ALPHABET = { 'a', 'b', 'c'}

FINAL_STATES = { 'C' }

STATE_TRAN = {
    ('A', 'b'): 'B',

    ('B', 'a'): 'B',
    ('B', 'c'): 'C',
    ('B', 'b'): 'D',

    ('C', 'a'): 'B',

    ('D', 'b'): 'A',
}

def automaton(states, initial, finals, input_string, transitions):
    state = initial

    for caracter in input_string:

        try:
            state = transitions[state, caracter]
        except KeyError:
            state = 'E'
            break

    return state

if __name__ == '__main__':

    input_string = sys.argv[1]

    final_state = automaton(
        STATES,
        INITIAL_STATE,
        FINAL_STATES,
        input_string,
        STATE_TRAN
    )
    
    print('Aceito' if final_state in FINAL_STATES else 'Rejeitado')
