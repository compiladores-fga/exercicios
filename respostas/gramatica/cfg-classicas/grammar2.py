from lark import Lark

# Q1.2
grammar = Lark(
    r"""
    start : group

    ?group : atom*

    ?atom : LSTRING
        |   "(" atom* ")"

    LSTRING: /L+/

    %ignore /\s+/
    """,
    parser="lalr"
)

exemplo = r"""
L(L(LL))
L
LLL
(LLLL)
(LLL)
((L))
(((L((((L)))LLL))LL))
"""


tree = grammar.parse(exemplo)
print(tree)
