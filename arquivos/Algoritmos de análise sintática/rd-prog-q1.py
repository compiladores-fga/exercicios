grammar = """
value : a
"""

import re
lex = re.compile(r"[a-z]+|[\[\],():]")

class Token(str):
    """docstring for Token"""
    def __repr__(self):
        value = super().__repr__()
        return value
        
    def __new__(cls, value, kind):
        tk = str.__new__(cls, value)
        tk.kind = kind
        return tk

REGEX_MAP = {
    "A"  : r"a",
    "WS"    : r"\s+",
    "ERRO"  : r".",

}

REGEX = re.compile("|".join(f"(?P<{i}>{j})" for i, j in REGEX_MAP.items()))

def lex(src) -> list:
    tokens = []
    for i in REGEX.finditer(src):
        kind = i.lastgroup
        value = src[i.start():i.end()]
        tk = Token(value, kind)
        if kind == "WS":
            continue
        elif kind == "ERRO":
            raise SyntaxError(f"Bad token: {value}")
        else:
            tokens.append(tk)
    return tokens

def parse(src):
    """
    Retorna valor a partir da representação como string.
    """
    tokens = lex(src)
    tokens.append("$")
    res = value(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res

def value(tokens):
    # Implemente a regra que lê uma lista de tokens e retorna um
    # valor da linguagem:
    #
    #   value : lst | var | pair 
    
    if tokens[0] == "a":
        return lst(tokens)
    elif tokens[0] == "$":
        return

    raise SyntaxError

def lst(tokens):
    # Processa listas:
    #
    #   lst   : "[" [value ("," value)*] "]"
    values = expect(["a", "$"], tokens)
    if tokens[0] != "$":
        values = value(tokens)
    return values

def expect(value, tokens):
    """
    Remove primeiro elemento da lista de tokens e produz um erro
    de sintaxe se o elemento não for igual a tk.
    """
    tk = tokens[0]
    tkf = tokens[1]
    if tk != value[0] or tkf != value[1]:
        raise SyntaxError(f"Bad token: {tk}")
    temp = tokens[0]
    readtk(tokens)
    return temp

def readtk(tokens):
    return tokens.pop(0)

src = "a"
# print(parse(src))
assert parse(src) == "a"