from lark import Lark, InlineTransformer

grammar = Lark(r"""
?start : expr
?expr  : expr "+" term     -> expr
       | term
?term  : term "*" atom     -> term
       | atom
?atom  : NUMBER            -> atom
       | "(" expr ")"
NUMBER : /\d+/
%ignore /\s+/
""")


class CalcTransformer(InlineTransformer):    
    def expr(self, *args):
        return ["+", *args] if len(args) > 1 else args

    def term(self, *args):
        return ["*", *args] if len(args) > 1 else args

    def atom(self, tk):
        return int(tk)
     


def ast(x):
    transformer = CalcTransformer()
    return transformer.transform(grammar.parse(x))

assert ast("42") == 42
assert ast("1 + 1") == ["+", 1, 1]
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]
