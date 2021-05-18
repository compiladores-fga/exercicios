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
    "op"  : r"[\[\],():]",
    "var" : r"[a-z]+",
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
    res = value(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def expect(tk, tokens):
    """
    Remove primeiro elemento da lista de tokens e produz um erro
    de sintaxe se o elemento não for igual a tk.
    """
    aux_tk = tokens[0]
    if aux_tk != tk:
        raise SyntaxError(f"Bad token: {aux_tk}")
    return tokens.pop(0)


def value(tokens):
    # Implemente a regra que lê uma lista de tokens e retorna um
    # valor da linguagem:
    #
    #   value : lst | var | pair 
    
    aux_token = tokens[0]

    if aux_token == "[":
        return lst(tokens)
    elif aux_token == "(":
        return pair(tokens)
    
    aux_token = tokens.pop(0)
    if aux_token.kind == "var":
        return aux_token



def lst(tokens):
    # Processa listas:
    #
    #   lst   : "[" [value ("," value)*] "]" 
    expect("[", tokens)
    if(tokens[0] == "]"):
        tokens.pop(0)
        return[]
    
    values = [value(tokens)]
    
    tk = tokens.pop(0)
    while tk == ",":
        values.append(value(tokens))
        tk = tokens.pop(0)
    if tk != "]":
        raise SyntaxError(f"Bad token: {tk}")

    return values



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