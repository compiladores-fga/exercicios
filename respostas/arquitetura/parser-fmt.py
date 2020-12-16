import sys

from lark import Lark, Transformer, v_args

json_grammar = r"""
    ?start: value
    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null
          | "Infinity"         -> inf
          | "-Infinity"        -> minf
          | "NaN"              -> nan
    array  : "[" [value ("," value)* ","?] "]"
    object : "{" [pair ("," pair)* ","?] "}"
    pair   : (string | no_quote_string) ":" value
    string : ESCAPED_STRING
    no_quote_string : /[A-Za-z_]+/
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    
    %ignore /\/\/.*/
"""

class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def no_quote_string(self, s):
        s = str(s[0])
        return s

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
    inf = lambda self, _: float("inf")
    minf = lambda self, _: -float("inf")
    nan = lambda self, _: float("nan")


json_parser = Lark(json_grammar, parser='lalr',
                   lexer='standard',
                   propagate_positions=False,
                   maybe_placeholders=False,
                   transformer=TreeToJson())
parse = json_parser.parse

def test():
    test_json = '''
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false }, //Comentario
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ,], //VírgulaFimLista
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ], ], //VírgulaFimLista
            "nothing"      : null,
            "constantsAccepted"    : [Infinity, -Infinity, NaN,] //VirgulaFimLista
        }
    '''

    j = parse(test_json)
    print(j)
    import json
    assert j == json.loads(test_json)


if __name__ == '__main__':
    try:
        test()
    #with open(sys.argv[1]) as f:
    #    print(parse(f.read()))
    except:
        ...