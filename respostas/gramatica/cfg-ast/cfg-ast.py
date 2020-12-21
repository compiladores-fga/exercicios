import re
import math
from lark import Lark, InlineTransformer, Token

# Implemente a gramática aqui! Você pode testar manualmente seu código executando
# o arquivo calc.py e testá-lo utilizando o pytest.
grammar = Lark(
    r"""
    ?start : expr
    
    ?expr : expr "+" term -> sum
         | term

    ?term : term "*" atom -> mul
         | atom
    
    ?atom : NUMBER   -> number
         | "(" expr ")"
    
    NUMBER : /\d+/
    %ignore /\s/
"""
)


class Tranform(InlineTransformer):
    def number(self, token):
        try:
            return int(token)
        except:
            return float(token)

    def sum(self, x, y):
        return {"op": "+", "left": x, "right": y}

    def mul(self, x, y):
        return {"op": "*", "left": x, "right": y}

    def start(self, *args):
        return args[-1]


transformer = Tranform()


def ast(x):
    tree = grammar.parse(x)
    tree = transformer.transform(tree)
    print(x)
    print(tree)
    print('-' * 40)
    return tree


assert ast("42") == 42
assert ast("1 + 1") == {"op": "+", "left": 1, "right": 1}
assert ast("1 + 2 * 3") == {"op": "+", "left": 1, "right": {"op": "*", "left": 2, "right": 3}}
