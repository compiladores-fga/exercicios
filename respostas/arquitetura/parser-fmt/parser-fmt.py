# parser-fmt
"""
Simple JSON Parser
==================
The code is short and clear, and outperforms every other parser (that's written in Python).
For an explanation, check out the JSON parser tutorial at /docs/json_tutorial.md
"""
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
          | inf
          | nan
    array  : "[" [value ("," value)* ","?] "]"
    object : "{" [pair ("," pair)* ","?] "}"
    pair   : string ":" value
           | optional ":" value
    
    ?inf   : "Infinity" -> infinity
           | "-Infinity" -> minus_infinity
           
    ?nan   : "NaN" -> not_a_number
    
    optional: /[a-zA-Z_]+/ -> optional_string
    string : ESCAPED_STRING
    
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    
    %ignore /\/\*(.|\n)+\*\//
    %ignore /[\/\/]{2}.*/
    
    %ignore WS
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def optional_string(self, token):
        token = str(token[0])
        return token

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    infinity = lambda self, _: float("inf")
    minus_infinity = lambda self, _: -float("inf")
    not_a_number = lambda self, _: float("nan")

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


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
    test_json = '''
        /*
            comentário mutilinha em c
        */
        {   
            // Eu sou um comentário em c
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false, },
            "numbers054"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7, ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
            "nothing"      : null,
            nome          : 20,
            infinity       : [Infinity],
            minusinfinity  : [-Infinity],
            notANumber     : [NaN, ]
        }
    '''

    j = parse(test_json)
    print(j)


if __name__ == '__main__':
    test()
