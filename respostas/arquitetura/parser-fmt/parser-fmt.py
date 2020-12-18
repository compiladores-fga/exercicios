import sys

from lark import Lark, Transformer, v_args

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

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
    pair   : (string | special) ":" value
    string : ESCAPED_STRING
    special : /[a-zA-Z_]+/

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    
    %ignore /\/\*(.|\n)+\*\//
    %ignore /\/\/.*/

    %ignore WS
"""


class TreeToJson(Transformer):
    @v_args(inline=True)    
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def special(self, key):
        key = str(key[0])
        return  key 

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
                   # Disabling propagate_positions and placeholders slightly improves speed
                   propagate_positions=False,
                   maybe_placeholders=False,
                   # Using an internal transformer is faster and more memory efficient
                   transformer=TreeToJson())
parse = json_parser.parse


def test():
    test_json = '''
        /* 
            multi
            line
            commentary
        */

        // commentary

        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false, },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b"]],
            //comment
            "nothing"      : null,
            "constants"    : [Infinity, -Infinity, NaN],
            "comma"        : [1, {"nome": "josé",}, 3,],
            special        : { infinity: Infinity }
        } 
    '''
    
    j = parse(test_json)
    pretty(j)


if __name__ == '__main__':
    test()