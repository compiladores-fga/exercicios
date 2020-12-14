from lark import Lark, InlineTransformer

grammar = Lark(
r"""
    ?start: expr 
    ?expr : expr "+" term -> add
        | term
    ?term : term "*" atom -> mul
        | atom
    ?atom : NUMBER -> number
        | "(" expr ")"
    NUMBER : /\d+/
    %ignore /\s+/
    %ignore /\#.*/
"""
)


class Transformer(InlineTransformer):
    def add(self, a, b):
        return ["+", a, b]

    def mul(self, a, b):
        return ["*", a, b]
    
    def number(self, token):
        return float(token)