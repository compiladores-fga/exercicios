## rd-prog

### Q1

```python
grammar = """
1.  S ⟶ + S S
2.  S ⟶ * S S
3.  S ⟶ ~ S
4.  S ⟶ n
"""

import re

lex = re.compile(r"\d+|[+\-*~]")


def parse(src):
    """
    Retorna valor a partir da representação como string.
    """
    tokens = [*lex.findall(src), "$"]
    res = value(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def expect(tk, tokens):
    """
    Remove primeiro elemento da lista de tokens e produz um erro
    de sintaxe se o elemento não for igual a tk.
    """
    tk_ = tokens.pop(0)
    if tk != tk_:
        raise SyntaxError(f"esperava {tk}, obteve {tk_}")


def value(tokens):
    # Implemente a regra que lê uma lista de tokens e retorna um
    # valor da linguagem:
    #
    #   value : lst | var | pair 
    
    if tokens[0] == "+":
        expect("+", tokens)
        left = value(tokens)
        right = value(tokens)
        return left + right

    if tokens[0] == "*":
        expect("*", tokens)
        left = value(tokens)
        right = value(tokens)
        return left * right

    if tokens[0] == "~":
        expect("~", tokens)
        number = value(tokens)
        return ~ number

    tk = tokens.pop(0)
    if tk.isdigit():
        return int(tk)

    raise SyntaxError
    

assert parse("+ 1 1") == 2
assert parse("* 1 1") == 1
assert parse("~ 0") == -1
assert parse("20") == 20
```

### Q2

```python
import re


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
    'LIST'    : r'[[\],():]',
    "VAR"     : r'[a-z]+',
    "WS"      : r'\s+',
    "ERROR"   : r'.',
}

REGEX = re.compile('|'.join(
    f'(?P<{k}>{v})' for k, v in REGEX_MAP.items()
))

def lex(src) -> list:
    tokens = []
    for m in REGEX.finditer(src):
        kind = m.lastgroup
        value = src[m.start():m.end()]
        tk = Token(value, kind)
        if kind == 'WS':
            continue
        elif kind == 'ERROR':
            raise SyntaxError(r'bad token: {tk}')
        else:
            tokens.append(tk)
    return tokens

def parse(src):
    """
    Retorna valor a partir da representação como string.
    """
    tokens = lex(src)
    tokens.append('$')
    res = value(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def expect(value, tokens):
    tk = peek(tokens)
    if tk != value:
        raise SyntaxError(r'bad token: {tk}')
    return read(tokens)

def start(tokens):
    """
    start  : object | array
    """
    if tokens[0] == '[':
        return lst(tokens)
    elif tokens[0] == '(':
        return pair(tokens)

    tk = read(tokens)
    if tk.kind == 'VAR':
        return tokens[0]

def value(tokens):
    # Implemente a regra que lê uma lista de tokens e retorna um
    # valor da linguagem:
    #
    #   value : lst | var | pair     
    if tokens[0] == '[':
        return lst(tokens)
    elif tokens[0] == '(':
        return pair(tokens)

    tk = read(tokens)
    if tk.kind == 'VAR':
        return tk

    raise SyntaxError

def peek(tokens):
    return tokens[0]

def lst(tokens):
    # Processa listas:
    #
    #   lst   : "[" [value ("," value)*] "]" 
    expect("[", tokens)
    if tokens[0] == "]":
        expect("]", tokens)
        return []

    values = [value(tokens)]
    
    tk = read(tokens)
    while tk == ',':
        values.append(value(tokens))
        tk = read(tokens)
    if tk != "]":
        raise SyntaxError(f'bad token: {tk}')
    
    return values

def read(tokens):
    return tokens.pop(0)

def pair(tokens):
    # Processa pares:
    # 
    #   pair  : "(" value ":" value ")" 
    expect("(", tokens)
    if tokens[0] == ")":
        expect(")", tokens)
        return ()

    tk = read(tokens)
    left = tk
    expect(":", tokens)
    right = value(tokens)
    tk = read(tokens)
    if tk != ")":
        raise SyntaxError(f'bad token: {tk}')
    return (left, right)

src = "[a,b,(c:d),[ab,cd,ef]]"
print(parse(src))
assert parse(src) == ["a", "b", ("c", "d"), ["ab", "cd", "ef"]]
``` 