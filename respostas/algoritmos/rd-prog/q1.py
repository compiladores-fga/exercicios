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
    tokens = lex(strr)
    tokens.append("$")
    res = S(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def expect(tk, tokens):
    aux_token = tokens.pop(0)
    if aux_token != tk:
        raise SyntaxError(f"Bad token: {aux_token}")


def S(tokens):
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
   

assert parse("1") == 1
assert parse("~ 1") == -2
assert parse("+ 5 5") == 10
assert parse("* 3 7") == 21
assert parse("+ 4 * 5 2") == 14
