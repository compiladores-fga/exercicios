state = None

def state_A(data):
    global state
    if (data == 'b'):
        state = state_B

def state_B(data):
    global state
    if (data == 'a'):
        state = state_B
    elif (data == 'b'):
        state = state_D
    elif (data == 'c'):
        state = state_C

def state_C(data):
    global state
    if (data == 'a'):
        state = state_B

def state_D(data):
    global state
    if (data == 'b'):
        state = state_A

def state_machine(data):
    global state
    state = state_A
    for c in data:
        print(f"State: {state}, Input: {c}")
        state(c)
        print(f"Next state: {state}")
        print()
    if state == state_D:
        print("Aceito")
        return True
    else:
        print("Rejeitado")
        return False

if __name__ == "__main__":
    data = input("Input string: ")
    state_machine(data)
