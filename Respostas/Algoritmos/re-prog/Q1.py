# Gramática G2
import re

grammar = """
S   : + S S
S   : * S S
S   : ~ S
S   : n

n   : /[\d]+/
"""

class Token(str):
    kind : str
    def __new__(cls, value, kind):
        tk = str.__new__(cls, value)
        tk.kind = kind
        return tk

    def __repr__(self):
        value = super().__repr__()
        return value

REGEX_MAP = {
    "n"   : r"[\d]+",
    "op"  : r"[+*~]",
    "ws"  : r"\s+",
    "erro": r"."
}


REGEX = re.compile("|".join(f"(?P<{i}>{j})" for i, j in REGEX_MAP.items()))

def lex(strr):
    tokens = []
    for m in REGEX.finditer(strr):
        kind = m.lastgroup
        value = strr[m.start():m.end()]
        tk = Token(value, kind)
        if kind == "ws":
            continue 
        elif kind == "erro":
            raise SyntaxError(r"Bad token: {tk}")
        else:
            tokens.append(tk)
    return tokens


def parse(strr):
    """
    Retorna valor a partir da representação como string.
    """
    tokens = lex(strr)
    tokens.append("$")
    res = S(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def expect(tk, tokens):
    """
    Remove primeiro elemento da lista de tokens e produz um erro
    de sintaxe se o elemento não for igual a tk.
    """
    aux_token = tokens.pop(0)
    if aux_token != tk:
        raise SyntaxError(f"Bad token: {aux_token}")


#def value
def S(tokens):
    # Implemente a regra que lê uma lista de tokens e retorna um
    # valor da linguagem:
    #
    #   value : lst | var | pair 
    
    tk = tokens[0]

    if tk == "+":
        tokens.pop(0)
        l = S(tokens)
        r = S(tokens)
        return l + r

    elif tk == "*":
        tokens.pop(0)
        l = S(tokens)
        r = S(tokens)
        return l * r 

    elif tk == "*":
        tokens.pop(0)
        l = S(tokens)
        r = S(tokens)
        return l * r

    elif tk == "~":
        tokens.pop(0)
        res = S(tokens)
        return ~ res
    
    tk = tokens.pop(0)
    if tk.kind == "n":
        return int(tk)
   

src_1 = "+ 1 2"
assert parse(src_1) == 3
src_11 = "+ 15 20"
assert parse(src_11) == 35
src_2 = "* 10 100"
assert parse(src_2) == 1000
src_22 = "* 2 8"
assert parse(src_22) == 16
src_3 = "~ 1"
assert parse(src_3) == -2
src_4 = "+ 2 * 5 5"
assert parse(src_4) == 27
src_5 = "84"
assert parse(src_5) == 84