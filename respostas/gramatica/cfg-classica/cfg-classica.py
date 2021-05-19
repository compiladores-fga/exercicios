from lark import Lark

# Strings formadas por n a's seguidas de n b's; n >= 1. 
# Ex.: aabb, ab, aaabbb.
strings_pareadas = r"""
start : a+b+
a: "a"
b: "b"
"""

# Letras L Dentro de parênteses pareados. 
# Ex.: LL, (LL), L(L(LL)), (((L)(L)))
letras_dentro_de_parenteses = r"""
start : L* (parenteses* L+ parenteses*)*
L: "L"
parenteses: "(" | ")"
"""


# Listas com elementos separados por vírgulas. 
# Ex.: [], [e], [e,e,e]
listas_com_elementos_separados_por_virgulas = r"""
start : cochetes+ (elemento*virgula*)* cochetes+
cochetes: "[" | "]"
elemento: "e"
virgula: ","
"""
    

# Elementos e listas que podem conter outras listas. 
# Ex.: e, [], [[]], [e], [e,[e,[]],e]
listas_aninhadas = r"""
start : conj* conjcochetes* (cochetes+conj*)*
conjcochetes: cochetes cochetes
cochetes: "[" | "]"
conj: (elemento+virgula*)
elemento: "e" | "" | 
virgula: ","
"""


# Expressões matemáticas no estilo prefixo. 
# Ex.: 42, + 1 2, + * 10 2 2
operadores_prefixos = r"""
start : "..."
"""

grammar = Lark(letras_dentro_de_parenteses)

code = "(LL)"

result = grammar.parse(code)
print(result.pretty())