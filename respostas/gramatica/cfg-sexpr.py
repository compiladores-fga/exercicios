import re
from lark import Lark, InlineTransformer, Token

grammar = Lark(
r"""
    ?start  : expr 
    ?expr   : expr "+" term -> add
            | term
    ?term   : term "*" atom -> mul
            | atom
    ?atom   : NUMBER -> number
            | "(" expr ")"

    NUMBER  : /\d+/

    %ignore /\s+/
    %ignore /\#.*/
"""
)

class Transformer(InlineTransformer):
    def add(self, expr, term):
        return ["+", expr, term]

    def mul(self, term, atom):
        return ["*", term, atom]
    
    def number(self, num):
        try:
            return int(num)
        except:
            return float(num)

transformer = Transformer()

def ast(x):
    return transformer.transform(grammar.parse(x))

print(ast("42") == 42)
print(ast("1 + 1") == ["+", 1, 1])
print(ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]])
