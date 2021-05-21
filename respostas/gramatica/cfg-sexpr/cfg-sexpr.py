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
        return ["+", x, y]

    def term(self, x, y):
        return ["*", x, y]

    def atom(self, token):
        return float(token)


transformer = Transformer()


def ast(x):
    return transformer.transform(grammar.parse(x))


assert ast("42") == 42
assert ast("1 + 1") == ["+", 1, 1]
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]
