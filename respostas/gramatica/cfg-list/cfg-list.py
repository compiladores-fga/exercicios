# Q1
from lark import Lark

grammar = Lark(r"""
                ?start  :   list
                ?list   :   "[" elem ("," elem)* "]"      -> json
                        |   "(" elem+ ")"                 -> lisp
                        |   "(" (elem ","?)+ ")"          -> lispii
                        |   "[" (elem ",")+ "]"           -> python
                        |   "[" (elem? ","+)+ "]"         -> javascript
                elem    :   /[^,\s\]\)]+/
                %ignore /\s+/
                """
               )

lists = [
        r"""[5, 4, 2, 0]       """,
        r"""(150 12 100 1)    """,
        r"""(8, 15 8, 155,)   """,
        r"""[7, 8, 2, 14,]      """,
        r"""[25,,,,,, 8,,, 10,, 56,]""",
        r"""[,]                """,
        ]

for list in lists:
    print(list)
    tree = grammar.parse(list)
    print(tree.pretty())
