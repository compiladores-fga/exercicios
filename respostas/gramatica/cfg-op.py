from lark import Lark

# **Q1)** Algumas linguagens de programação possuem operadores de composição e aplicação de funções. Por exemplo, em Elm e F#, a expressão `x |> f` significa executar a função `f` com o argumento `x`. Este operador é associativo à esquerda `x |> f |> g = (x |> f) |> g`. Já `f >> g` cria uma nova função que passa o argumento para f e o resultado disto para g. Este operador também é associativo à esquerda e possui uma precedência maior que `|>`, de forma que `x |> f >> g >> h |> w` pode ser interpretado como `(x |> ((f >> g) >> h)) |> w`.

# Crie uma gramática para uma mini linguagem que inclua estes operadores e nomes como `x`, `y`, `f`, `g`, etc como símbolos terminais. Certifique-se que a gramática proposta obedece às leis de associatividade e precedência descritas acima. 

q11 = r"""
    start       : operation
    operation   : item opetation2 item | item operation1 item
    opetation1  : ">>"
    operation2  : "|>"
    item        : name | operation
    name        : "x" | "y" | "f" | "g" | "h" | "w"
"""

grammar = Lark(q11)

examples = ["x |> f >> g >> h |> w"]

for example in examples:
    result = grammar.parse(example.replace(' ', ''))
    print(result.pretty())