from lark import Lark
import pprint

grammar = Lark(r"""
    ?start  :   list

    ?list   :   "[" elem ("," elem)* "]"          -> json
            |   "(" elem+ ")"                     -> lisp
            |   "(" (elem ","?)+ ")"              -> lispii
            |   "[" (elem ",")+ "]"               -> python
            |   "[" (elem? ","+)+ "]"             -> javascript

    elem    :   /[^,\s\]\)]+/

    %ignore /\s+/
""")

tests = [
            r"""[1, 2, 3, 4]       """, # json
            r"""(4000 300 20 1)    """, # lisp
            r"""(10, 10 10, 10,)   """, # lispii-2
            r"""[0, 2, 4, 6,]      """, # python
            r"""[4,,,, 3,,, 2,, 1,]""", # javascript
            r"""[,]                """, # javascript
]

for test in tests:
    print("Rodando teste:", test)
    tree = grammar.parse(test)
    print(tree.pretty()) 