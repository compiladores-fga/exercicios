#Cfg-List Questão 1

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