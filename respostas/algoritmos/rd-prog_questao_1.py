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
