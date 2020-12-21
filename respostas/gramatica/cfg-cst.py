from lark import Lark

GRAMMAR = r"""
?start : expr

expr : expr "+" term
     | term

term : term "*" atom
     | atom

atom : NUMBER
     | "(" expr ")"

NUMBER : /\d+/
%ignore /\s+/
"""

srcs = ['42',  '2 * (11 + 2 * 5)']
grammar = Lark(GRAMMAR)


for src in srcs:
    print('*'*30, src, '*'*30)
    tree = grammar.parse(src)
    print(tree.pretty())