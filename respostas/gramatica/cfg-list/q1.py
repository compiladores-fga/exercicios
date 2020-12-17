from lark import Lark

grammar = Lark(r"""
?start  :   list

?list   :   "[" ELEM ("," ELEM)* "]" -> json
        |   "[" (ELEM? ","+)+ "]" -> js
        |   "[" (ELEM ",")+ "]" -> python
        |   "(" ELEM+ ")" -> lisp
        |   "(" (ELEM ","?)+ ")" -> lispii
ELEM    :   /[^\,\s\)\]]+/

%ignore /\s+/
""")

exemplos = [
  "[1, 2, 3]",
  "(1 2 3)",
  "(1, 2, 3,)",
  "[1, 2, 3,]",
  "[1,2,,3,,,]"
]

for ex in exemplos:
    tree = grammar.parse(ex)
    print(tree)