from lark import Lark

# **Q1)** Crie gramáticas livres de contexto (utilizndo o Lark ou simplesmente a sintaxe EBNF) que identifiquem as seguintes linguagens:

# 1. Strings formadas por n a's seguidas de n b's; n >= 1. Ex.: `aabb, ab, aaabbb`.
q11 = r"""
    start: ab
    ab: "a" ab "b"| "ab"
"""

grammar = Lark(q11)

examples = ["aabb", "ab", "aaabbb"]

for example in examples:
    result = grammar.parse(example)
    print(result.pretty())

# 2. Letras L Dentro de parênteses pareados. Ex.: `LL, (LL), L(L(LL)), (((L)))`
q12 = r"""
start : exp
exp   : let | tuple
let   : let exp | exp let | "L"
tuple : tuple exp | exp tuple | "(" exp ")"
"""


grammar = Lark(q12)

examples = ["LL", "(LL)", "L(L(LL))", "(((L)))"]

for example in examples:
    result = grammar.parse(example)
    print(result.pretty())



# 3. Listas com elementos separados por vírgulas. Ex.: `[], [e], [e,e,e]`
listas_com_elementos_separados_por_virgulas = r"""
start : exp
exp   : "[" e "]" | "[" "]"
e     : "e" | "e" "," e 
"""
grammar = Lark(listas_com_elementos_separados_por_virgulas)

examples = ["[]", "[e]", "[e,e,e]"]

for example in examples:
    result = grammar.parse(example)
    print(result.pretty())


# 4. Listas que podem conter outras listas. Ex.: `[], [[]], [e], [e,[e,[]],e]`
listas_aninhadas = r"""
start : exp
exp   : "e" | list
list  : "[" items? "]"
items : exp | items | items "," items
"""

grammar = Lark(listas_aninhadas)

examples = ["[]", "[[]]", "[e]", "[e,[e,[]],e]"]

for example in examples:
    result = grammar.parse(example)
    print(result.pretty())


# 5. Expressões matemáticas no estilo prefixo. Ex.: `42, + 1 2, + * 10 2 2` 
operadores_prefixos = r"""
start   : exp
exp     : bop | NUMBER
bop     : bopr " " exp " " exp 
bopr    : "+" | "-" | "*" | "/" | "^"

%import common.NUMBER -> NUMBER
"""

grammar = Lark(operadores_prefixos)

examples = ["42", "+ 1 2", "+ * 10 2 2"]

for example in examples:
    result = grammar.parse(example)
    print(result.pretty())