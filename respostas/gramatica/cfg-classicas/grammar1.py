from lark import Lark

# Q1.1
grammar = Lark(
    r"""
    start : atom*

    ?atom : STRING

    STRING: /a+b+/

    %ignore /\s+/
    """,
    parser="lalr",
)

exemplo = r"""
aaaabbbb
abbbb
aaaaaabbbb
"""


tree = grammar.parse(exemplo)
print(tree)
