from lark import Lark

# Q1.4
grammar = Lark(
    r"""
    start : value*

    ?value: list

    ?list: "[" list  ("," list)* "]"
        |   "[" "]"
        |   ELEMENT


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
[[[[]]]]
[e,[e,[]],e]
[[e, e, e, [[[e, e, []]]]]]
"""


tree = grammar.parse(exemplo)
print(tree)
