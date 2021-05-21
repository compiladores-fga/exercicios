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
        return {"op": "+", "left": x, "right": y}

    def multiplicacao(self, x, y):
        return {"op": "*", "left": x, "right": y}

    def numero(self, token):
        return float(token)


def ast(src):
    transformer = Transformer()
    return transformer.transform(grammar.parse(src))

assert ast("42") == 42
assert ast("1 + 1") == {"op": "+", "left": 1, "right": 1} 
assert ast("1 + 2 * 3") == {"op": "+", "left": 1, "right": {"op": "*", "left": 2, "right": 3}}
# print(ast("42"))

# referência https://github.com/DaviAntonio/exercicios/blob/master/respostas/gramatica/cfg-list/q2.py
# referência https://github.com/CaioNunes/exercicios/blob/master/respostas/gramatica/cfg-sexpr.py