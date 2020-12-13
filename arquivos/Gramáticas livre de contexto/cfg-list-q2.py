import re
from lark import Lark, InlineTransformer
from typing import NamedTuple

grammar = Lark(
    r"""
?start      : gramatica

?gramatica  : "[" (item|undefined|gramatica) ("," (item|gramatica)|undefined)* ","? "]" -> gramatica
?undefined  : ","                                                                       -> undefined
?item       : ITEMS                                                                     -> item

ITEMS       : "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
%ignore /\s+/
""")


class LispyTransformer(InlineTransformer):
    def gramatica(self, *tokens):
        return list(tokens)
    def undefined(self):
        return 'None'
    def item(self, tokens):
        return int(tokens.value)

test = r"""
    [1,,2,[,,],]
"""

transformer = LispyTransformer()
tree = grammar.parse(test)
value = transformer.transform(tree)
print(value)