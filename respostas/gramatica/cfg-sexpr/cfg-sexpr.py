from lark import Lark, InlineTransformer


grammar = Lark(
    r"""
    start: expr
    ?expr : expr "+" term -> expr
        | term

    ?term : term "*" atom -> term
        | atom

    ?atom : NUMBER -> number
        | "(" expr ")"

    NUMBER : /\d+/

    %ignore /\s+/
    """,
    parser="lalr"
)


class Transformer(InlineTransformer):
    def start(self, *args):
        return args[-1]

    def expr(self, *args):
        return ['+', *args]

    def term(self, *args):
        return ['*', *args]

    def number(self, value):
        try:
            return int(value)
        except ValueError:
            return float(value)


transformer = Transformer()


def ast(x):
    return transformer.transform(grammar.parse(x))


print('Realizando casos de teste...')
print(ast("42"))
assert ast("42") == 42

print(ast("1 + 1"))
assert ast("1 + 1") == ["+", 1, 1]

print(ast("1 + 2 * 3"))
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]
