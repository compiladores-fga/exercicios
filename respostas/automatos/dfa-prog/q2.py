state = None


def state_A(data):
    """ Estado A do autômato."""
    global state
    if data == "b":
        state = state_B


def state_B(data):
    """ Estado B do autômato."""
    global state
    if data == "a":
        state = state_B
    elif data == "b":
        state = state_D
    elif data == "c":
        state = state_C


def state_C(data):
    """ Estado C do autômato."""
    global state
    if data == "a":
        state = state_B


def state_D(data):
    """ Estado D do autômato."""
    global state
    if data == "b":
        state = state_A


def state_machine(data):
    """Executa o autômato finito determinístico
    Implementado como uma máquina de estados finitos onde cada estado é
    uma função
    A funçção a ser executada é determinada pela variável global state
    Ao final da execução, verifica-se se o estado final é um estado de
    aceitação.
    Se é um estado de aceitação, retorna True. Caso não seja, retorna False
    """
    global state
    state = state_B
    for c in data:
        print(f"State: {state}, Input: {c}")
        state(c)
        print(f"Next state: {state}")
        print()
    if state == state_C:
        print("Aceito")
        return True
    else:
        print("Rejeitado")
        return False


if __name__ == "__main__":
    data = input("Input string: ")
    state_machine(data)
