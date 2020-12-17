#parser-fmt 
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
          | "Infinity"         -> inf
          | "-Infinity"        -> minf
          | "NaN"              -> nan
    array  : "[" [value ("," value)* ","?] "]"
    object : "{" [pair ("," pair)* ","?] "}"
    pair   : (string | name) ":" value
    string : ESCAPED_STRING
    name : /[a-zA-Z_]+/
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    
    %ignore /\/\/.*/
    %ignore WS
"""


class TreeToJson(Transformer):
    @v_args(inline=True)    
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def name(self, key):
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
        //comment
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false, },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b"]],
            //comment
            "nothing"      : null,
            "consts"       : [Infinity, -Infinity, NaN],
            "comma"        : [Infinity,],
            name           : 42,
            all            : [Infinity, {nothing : NaN,},] //comment
            //comment
        } 
        //comment
    '''

    j = parse(test_json)
    print(j)
    import json
    #assert j == json.loads(test_json)


if __name__ == '__main__':
    test()
    #with open(sys.argv[1]) as f:
    #    print(parse(f.read()))