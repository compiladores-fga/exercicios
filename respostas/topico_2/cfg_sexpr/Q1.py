#cfg_sexpr

from lark import Lark, InlineTransformer

grammar = Lark(r"""
?start: expr

?expr : expr "+" term -> expr
     | term

?term : term "*" atom -> term
     | atom

?atom : NUMBER        -> number
     | "(" expr ")"

NUMBER : /\d+/
%ignore /\s+/
""")

class Transformer(InlineTransformer):
    def expr(self, *args):
        if len(args) > 1:
            return ["+"] + list(args)
        else:
            return args
    
    def term(self, *args):
        if len(args) > 1:
            return ["*"] + list(args)
        else:
            return args
    
    def number(self, token):
        return float(token)

transformer = Transformer()

def ast(x):
    return transformer.transform(grammar.parse(x))

assert ast("42") == 42
assert ast("1 + 1") == ["+", 1, 1]
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]