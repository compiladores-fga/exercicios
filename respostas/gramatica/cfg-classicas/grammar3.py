from lark import Lark

# Q1.3
grammar = Lark(
    r"""
    start : value*

    ?value: ELEMENT
        |   "[" ELEMENT  ("," ELEMENT)* "]"
        |   "[" "]"

    ELEMENT: /e/

    %ignore /\s+/
    """,
    parser="lalr"
)

exemplo = r"""
e
[e]
[e, e]
[e, e, e, e, e]
[]
"""


tree = grammar.parse(exemplo)
print(tree)
