grammar = """
value : lst | var | pair
lst   : "[" [value ("," value)*] "]"
pair  : "(" value ":" value ")"
var   : /[a-z]+/
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
    "LIST"  : r"[\[\],():]",
    "VAR"   : r"[a-z]+",
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
    
    if tokens[0] == "[":
        return lst(tokens)
    elif tokens[0] == "(":
        tokens.pop(0)
        return tupl(tokens)

    tk = tokens.pop(0)
    if tk.kind == "VAR":
        return tk

    raise SyntaxError

def lst(tokens):
    # Processa listas:
    #
    #   lst   : "[" [value ("," value)*] "]" 
    expect("[", tokens)
    if tokens[0] == "]":
        expect("]", tokens)
        return []

    values = [value(tokens)]

    tk = tokens.pop(0)
    while tk == ",":
        values.append(value(tokens))
        tk = tokens.pop(0)
    if tk != "]":
        raise SyntaxError(f"Bad token: {tk}")

    return values

def expect(value, tokens):
    """
    Remove primeiro elemento da lista de tokens e produz um erro
    de sintaxe se o elemento não for igual a tk.
    """
    tk = tokens[0]
    if tk != value:
        raise SyntaxError(f"Bad token: {tk}")
    return tokens.pop(0)

def tupl(tokens):
    tuples = (pair(tokens))
    tk = tokens.pop(0)
    while tk == ".":
        tuples.append(pair(tokens))
        tk = tokens.pop(0)
    if tk != ")":
        raise SyntaxError(f"Bad token: {tk}")
    return tuples

def lis(tokens):
    lis = [pair(tokens)]
    tk = tokens.pop(0)
    while tk == ".":
        lis.append(pair(tokens))
        tk = tokens.pop(0)
    if tk != ")":
        raise SyntaxError(f"Bad token: {tk}")
    return lis

def pair(tokens):
    # Processa pares:
    # 
    #   pair  : "(" value ":" value ")" 
    tk = tokens.pop(0)
    if tk.kind != "VAR":
        raise SyntaxError(f"Bad token: {tk}")
    left = tk
    expect(":", tokens)
    right = value(tokens)
    return (left, right)

src = "[a,b,(c:d),[ab,cd,eg]]"
# print(parse(src))
assert parse(src) == ["a", "b", ("c", "d"), ["ab", "cd", "eg"]]