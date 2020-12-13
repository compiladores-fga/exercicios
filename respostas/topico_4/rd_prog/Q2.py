#rd_prog

import re

grammar = """
value : lst | var | pair
lst   : "[" [value ("," value)*] "]"
pair  : "(" value ":" value ")"
var   : /[a-z]+/
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
    "var" : r"[a-z]+",
    "op"  : r"[\[\],():]",
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
    res = value(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def value(tokens):
    # Implemente a regra que lê uma lista de tokens e retorna um
    # valor da linguagem:
    #
    #   value : lst | var | pair 
    tk = peek(tokens)

    if tk == "[":
        return lst(tokens)
    elif tk == "(":
        return pair(tokens) 
    
    tk = read(tokens)
    if tk.kind == "var":
        return tk



def lst(tokens):
    # Processa listas:
    #
    #   lst   : "[" [value ("," value)*] "]" 
    expect("[", tokens)
    if(peek(tokens) == "]"):
        read(tokens)
        return[]
    
    arr = [value(tokens)]
    
    tk = read(tokens)
    while tk == ",":
        arr.append(value(tokens))
        tk = read(tokens)
        
    return arr

def pair(tokens):
    # Processa pares:
    # 
    #   pair  : "(" value ":" value ")" 
    expect("(", tokens)
    left = value(tokens)
    expect(":", tokens)
    right = value(tokens)
    expect(")", tokens)

    return (left, right)

src = "[a,b,(c:d),[ab,cd,ef]]"
assert parse(src) == ["a", "b", ("c", "d"), ["ab", "cd", "ef"]]