#cfg-list - Q1
from lark import Lark

grammar = Lark(r"""
?start  :   list

?list   :   "[" elem ("," elem)* "]"      -> json
        |   "(" elem+ ")"                 -> lisp
        |   "(" (elem ","?)+ ")"          -> lispii
        |   "[" (elem ",")+ "]"           -> python
        |   "[" (elem? ","+)+ "]"         -> js

elem    :   /[^,\s\]\)]+/

%ignore /\s+/
""")

tests = [
            r"""[1, 2, 3, 4]       """,
            r"""(4000 300 20 1)    """,
            r"""(10, 10 10, 10,)   """,
            r"""[0, 2, 4, 6,]      """,
            r"""[4,,,, 3,,, 2,, 1,]""", 
            r"""[,]                """,
]


for test in tests:
    print(test)
    tree = grammar.parse(test)
    print(tree.pretty())