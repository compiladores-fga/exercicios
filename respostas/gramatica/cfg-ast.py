from lark import Lark, InlineTransformer

grammar = Lark(r"""
    ?start : expr

    ?expr  : expr "+" term -> expr
        | term

    ?term  : term "*" atom -> term
        | atom

    ?atom  : NUMBER        -> atom
        | "(" expr ")"

    NUMBER : /\d+/
    %ignore /\s+/

""")

class Transformer(InlineTransformer):
    def expr(self, x, y):
        return {"op": "+", "left": x, "right": y}

    def term(self, x, y):
        return {"op": "*", "left": x, "right": y}

    def atom(self, token):
        return float(token)

transformer = Transformer()

def ast(src):
    return transformer.transform(grammar.parse(src))

assert ast("42") == 42
assert ast("1 + 1") == {"op": "+", "left": 1, "right": 1} 
assert ast("1 + 2 * 3") == {"op": "+", "left": 1, "right": {"op": "*", "left": 2, "right": 3}}