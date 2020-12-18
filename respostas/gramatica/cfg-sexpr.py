import re
from lark import Lark, InlineTransformer
from typing import NamedTuple
import math
import re

class Symbol(NamedTuple):
    value: str

grammar = Lark(r"""
?start  :   expr            -> start               

?expr   : expr "+" term     -> soma
        |   term

?term   : term "*" atom     -> pow
        |   atom

?atom   :   NUMBER          -> number
        | "(" expr ")"      -> listing

NUMBER  :   /\d+/
%ignore /\s+/
""")

class LispyTransformer(InlineTransformer):

    def start(self, x):
        return x

    def soma(self, x, y):
        return list(["+", x, y])

    def pow(self, x, y):
        return list(["*", x, y])

    def number(self, x):
        return int(x)

    def listing(self, x):
        return list([x])

transformer = LispyTransformer()

def ast(src):
    retornar_funcao = transformer.transform(grammar.parse(src))
    print("src: ", src, " Retorno: ", retornar_funcao)
    return retornar_funcao

assert ast("42") == 42
assert ast("1 + 1") == ["+", 1, 1]
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]
