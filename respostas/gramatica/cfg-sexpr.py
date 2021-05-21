from lark import Lark, InlineTransformer, Token

grammar = Lark(
        r"""
        ?start : expr
        ?expr : expr "+" term -> soma
            | term

        ?term : term "*" atom -> multiplicacao
            | atom

        ?atom : NUMBER -> numero
            | "(" expr ")"

        NUMBER : /\d+/
        %ignore /\s/
        """,
        )

class Transformer(InlineTransformer):
    def soma(self, x, y):
        return ["+", x, y]

    def multiplicacao(self, x, y):
        return ["*", x, y]

    def numero(self, token):
        return float(token)


def ast(src):
    transformer = Transformer()
    return transformer.transform(grammar.parse(src))

assert ast("42") == 42
assert ast("1 + 1") == ["+", 1, 1]
assert ast("1 + 2 * 3") == ["+", 1, ["*", 2, 3]]

# referência https://github.com/DaviAntonio/exercicios/blob/master/respostas/gramatica/cfg-list/q2.py
# referência https://github.com/CaioNunes/exercicios/blob/master/respostas/gramatica/cfg-sexpr.py