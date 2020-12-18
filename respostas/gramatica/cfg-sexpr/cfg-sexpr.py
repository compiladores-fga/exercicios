from lark import Lark, InlineTransformer

grammar = Lark(r"""
start: expr

?expr : expr "+" term -> add
      | term

?term : term "*" atom -> mul
      | atom

?atom : NUMBER -> number
      | "(" expr ")"

NUMBER : /\d+/
%ignore /\s+/
%ignore /\#.*/
""")

class Transformer(InlineTransformer):
    def add(self, *args):
        return ['+', *args]

    def mul(self, *args):
        return ['*', *args]

    def number(self, value):
        try:
            return int(value)
        except ValueError:
            return float(value)
    
    def start(self, *args):
        return args[-1]