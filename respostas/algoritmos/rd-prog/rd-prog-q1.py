import re

grammar = """
    S   : + S S
    S   : * S S
    S   : ~ S
    S   : n

    n   : /[0-9]+/
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
    "n"   : r"[0-9]+",
    "op"  : r"[+*~]",
    "ws"  : r"\s+",
    "erro": r"."
}


REGEX = re.compile("|".join(f"(?P<{k}>{v})" for k, v in REGEX_MAP.items()))

def lex(str):
    tokens = []
    for m in REGEX.finditer(str):
        kind = m.lastgroup
        value = str[m.start():m.end()]
        tk = Token(value, kind)
        if kind == "ws":
            continue 
        elif kind == "erro":
            raise SyntaxError(r"Bad token: {tk}")
        else:
            tokens.append(tk)
    return tokens


def parse(str):
    tokens = lex(str)
    tokens.append("$")
    res = S(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def expect(token, tokens):
    aux_token = tokens.pop(0)
    if aux_token != token:
        raise SyntaxError(f"Bad token: {aux_token}")


def S(tokens):
    tk = tokens[0]

    if tk == "+":
        tokens.pop(0)
        left = S(tokens)
        right = S(tokens)
        return left + right

    elif tk == "*":
        tokens.pop(0)
        left = S(tokens)
        right = S(tokens)
        return left * right 

    elif tk == "*":
        tokens.pop(0)
        left = S(tokens)
        right = S(tokens)
        return left * right

    elif tk == "~":
        tokens.pop(0)
        res = S(tokens)
        return ~ res
    
    tk = tokens.pop(0)
    if tk.kind == "n":
        return int(tk)


src1 = "~ 1"
src2 = "+ 3 3"
src3 = "* 2 6"
src4 = "+ 7 * 2 5"
src5 = "50"

assert parse(src1) == -2
assert parse(src2) == 6
assert parse(src3) == 12
assert parse(src4) == 17
assert parse(src5) == 50