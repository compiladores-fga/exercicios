"""
Simple JSON Parser
==================
The code is short and clear, and outperforms every other parser (that's written in Python).
For an explanation, check out the JSON parser tutorial at /docs/json_tutorial.md
"""
import sys

from lark import Lark, Transformer, v_args

# Aceita comentários no estilo C (// como este!)
# Aceita uma vírgula opcional após os elementos de uma lista ou objeto: [1, {"n": 42,}, 3,]. A vírgula não pode aparecer em objetos e listas vazios.
# As aspas em strings são opcionais para nomes contendo apenas letras ou underscore.
# Também aceita as constantes Infinity, -Infinity e NaN para representar respectivamente float("inf"), -float("inf") e float("nan").

json_grammar = r"""
    ?start: value

    ?value: object
          | array
          | string
          | SIGNED_NUMBER         -> number
          | "true"                -> true
          | "false"               -> false
          | "null"                -> null
          | "Infinity"            -> infinity
          | "-Infinity"           -> minfinity
          | "NaN"                 -> nan

    ?array   : "[" [value ("," value)*] "]"
            |  "[" [value ("," value)* "," ] "]"

    ?object  : "{" [pair ("," pair)*] "}"
            | "{" [pair ("," pair)* "," ] "}"

    ?pair    : string ":" value

    ?string    : STRING                 -> string
              | STRINGSAS               -> stringsas
              | comment STRING          -> stringcomments
              | comment STRINGSAS       -> stringsascomments

    STRING    : /"[a-zA-Z0-9_\s"\\]+"/
    STRINGSAS : /[a-zA-Z0-9_]+/

    comment   : COMMENTS                -> comment
    COMMENTS  : /\/\/.*/

    %import common.SIGNED_NUMBER
    %ignore /\s/
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def stringsas(self, s):
      return str(s)
    def string(self, s):
      s = s[0]
      return s[1:-1].replace('\\"', '"')

    def stringsascomments(self, s):
      return str(s[1])
    def stringcomments(self, s):
      s = s[1]
      return s[1:-1].replace('\\"', '"')

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
    infinity = lambda self, _: float("inf")
    minfinity = lambda self, _: -float("inf")
    nan = lambda self, _: float("nan")
    comment = lambda self, _: ""

### Create the JSON parser with Lark, using the Earley algorithm
# json_parser = Lark(json_grammar, parser='earley', lexer='standard')
# def parse(x):
#     return TreeToJson().transform(json_parser.parse(x))

### Create the JSON parser with Lark, using the LALR algorithm
json_parser = Lark(json_grammar, parser='lalr',
                   # Using the standard lexer isn't required, and isn't usually recommended.
                   # But, it's good enough for JSON, and it's slightly faster.
                   lexer='standard',
                   # Disabling propagate_positions and placeholders slightly improves speed
                   propagate_positions=False,
                   maybe_placeholders=False,
                   # Using an internal transformer is faster and more memory efficient
                   transformer=TreeToJson())
parse = json_parser.parse


def test():
    test_json = r'''
        {
            "empty_object" : {},//asdadsd
            "empty_array"  : [],//dfd fdghdfhg
            booleans     : { "YES" : true, "NO" : false, },
            "numbers"      : [ Infinity, -Infinity, NaN, 0, 1, -2, 3.3, 4.4e5, 6.6e-7, ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ], ],
            "nothing"      : null
        }
    '''

    j = parse(test_json)
    print(j)
    import json
    assert j == json.loads(test_json)


if __name__ == '__main__':
    try:
      test()
      # with open(sys.argv[1]) as f:
      #   print(parse(f.read()))
    except:
      ...