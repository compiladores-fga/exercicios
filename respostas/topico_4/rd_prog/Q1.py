#rd_prog

#Implementação da gramática G2
#Considerei "n" como um numero natural para poder retornar um valor para as operações  

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

def lex(st):
    tokens = []
    for m in REGEX.finditer(st):
        kind = m.lastgroup
        value = st[m.start():m.end()]
        tk = Token(value, kind)
        if kind == "ws":
            continue 
        elif kind == "erro":
            raise SyntaxError(r"bad token: {tk}")
        else:
            tokens.append(tk)
    
    return tokens

def peek(tokens):
    return tokens[0]

def read(tokens):
    return tokens.pop(0)

def expect(tk, tokens):
    """
    Remove primeiro elemento da lista de tokens e produz um erro
    de sintaxe se o elemento não for igual a tk.
    """
    _tk = peek(tokens)
    if _tk != tk:
        raise SyntaxError(r"bad token: {tk}")
    
    return read(tokens)
        

def parse(st):
    """
    Retorna valor a partir da representação como string.
    """
    tokens = lex(st)
    tokens.append("$")
    res = S(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def S(tokens):
    tk = peek(tokens)

    if tk == "+":
        read(tokens)
        left = S(tokens)
        right = S(tokens)
        return left + right
    elif tk == "*":
        read(tokens)
        left = S(tokens)
        right = S(tokens)
        return left * right 
    elif tk == "*":
        read(tokens)
        left = S(tokens)
        right = S(tokens)
        return left * right
    elif tk == "~":
        read(tokens)
        value = S(tokens)
        return ~ value
    
    tk = read(tokens)
    if tk.kind == "n":
        return int(tk)

src1 = "+ 2 2"
src2 = "* 3 5"
src3 = "~ 1"
src4 = "+ 2 * 2 3"
src5 = "* ~0 + 4 2"

assert parse(src1) == 4
assert parse(src2) == 15
assert parse(src3) == -2
assert parse(src4) == 8
assert parse(src5) == -6