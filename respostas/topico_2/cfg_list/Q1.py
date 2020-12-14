#cfg_list

from lark import Lark

grammar = Lark(r"""
?start  :   list

?list   :   "[" ELEM ("," ELEM)* "]" -> json
        |   "(" ELEM+ ")" -> lisp
        |   "(" (ELEM ","?)+ ")" -> lispii
        |   "[" (ELEM ",")+ "]" -> python
        |   "[" (ELEM? ","+)+ "]" -> js

ELEM    :   /[^,\s\]\)]+/

%ignore /\s+/
""")

exemplos = [r"""
                [1, 2, 3, 4] 
            """,
            r"""
                (1 2 3 4)
            """,
            r"""
                (1, 2, 3, 4,)
            """,
            r"""
                [1, 2, 3, 4, ]
            """,
            r"""
                [1, 2,, 3,,, 4,,,,]
            """, 
            r"""
                [,]
            """,
]


for exemplo in exemplos:
    print(exemplo)
    tree = grammar.parse(exemplo)
    print(tree.pretty())