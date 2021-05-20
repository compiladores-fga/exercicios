import math

from lark import Lark, Transformer, v_args

GRAMMAR = r"""
    ?start: value
    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null
          | "NaN"              -> nan
          | "Infinity"         -> infinity
          | "-Infinity"        -> minus_infinity
    array    : "[" [value ("," value)* ","?]  "]"
    object   : "{" [pair ("," pair)* ","?]  "}"
    pair     : string ":" value
    string   : ESCAPED_STRING
             | /[a-z_A-Z]+/
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore /\/\/[^\n]*/
    %ignore WS
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def infinity(self, tk):
        return math.inf

    def minus_infinity(self, tk):
        return -math.inf

    def nan(self, tk):
        return math.nan

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


json_parser = Lark(GRAMMAR, parser='lalr',
                   lexer='standard',
                   propagate_positions=False,
                   maybe_placeholders=False,
                   transformer=TreeToJson())
parse = json_parser.parse


def test():
    json_test = '''
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false, },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7, ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
            "nothing"      : null,
            "mybooleans"   : { YES : true, "NO" : false, },
            "myconsts"     : { "inf": Infinity, "minusinf": -Infinity, "nan": NaN},
            "mynan"        : { "nan": NaN}
        }
    '''

    print(parse(json_test))


if __name__ == '__main__':
    test()
