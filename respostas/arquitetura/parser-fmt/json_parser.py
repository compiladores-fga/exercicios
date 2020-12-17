"""
Simple JSON Parser
==================

The code is short and clear, and outperforms every other parser (that's written in Python).
For an explanation, check out the JSON parser tutorial at /docs/json_tutorial.md
"""
import sys

from lark import Lark, Transformer, v_args, exceptions

json_grammar = r"""
    ?start: value

    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null
          | "Infinity"         -> positive_infinity
          | "-Infinity"        -> negative_infinity
          | "NaN"              -> not_a_number

    array  : "[" [value ("," value)* ","?] "]"
    object : "{" [pair ("," pair)* ","?] "}"
    pair   : (string | simple_id) ":" value

    string : ESCAPED_STRING

    COMMENT : /\/\/[^\n]*/
    simple_id : /[a-zA-Z_]+/

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %import common.CNAME

    %ignore WS
    %ignore COMMENT
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def simple_id(self, s):
        return str(s[0].value)

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

    positive_infinity = lambda self, _: float("inf")
    negative_infinity = lambda self, _: -float("inf")
    not_a_number = lambda self, _: float("nan")


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
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
            "nothing"      : null
        }
    '''

    j_old = parse(test_json)
    print(j_old)
    import json
    assert j_old == json.loads(test_json)
    print()
    test_json = '''
        // This is a test object
        {
            empty_object : {}, // Empty object (without double quotes)
            "empty_array"  : [], // Empty array
            "booleans"     : { "YES" : true, "NO" : false }, // Object of booleans (no optional comma)
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7, ], // Number array (with optional comma)
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ], // Nested string array
            "nothing"      : null, // Optional comma
        }
    '''
    j_new = parse(test_json)
    print(j_new)
    assert j_new == j_old

    print("Should fail:")
    to_fail = '''
        {
            "empty_object" : {,},
            "empty_array" : [,]
        }
    '''
    try:
        j_fail = parse(to_fail)
        print(j_fail)
    except exceptions.UnexpectedToken as e:
        print(f"Failed as expected with {e}")
    else:
        print("Unexpected successful parsing")
        assert None

    print("Try with infinity and NaN")
    expected = {"odd_list" : [float("inf"), -float("inf"), float("nan"), float(0)]}
    test_inf_nan = '''
        // Test with Infinity and NaN
        {
            odd_list : [Infinity, -Infinity, NaN, 0,]
        }
    '''
    j_inf_nan = parse(test_inf_nan)
    print(j_inf_nan)

if __name__ == '__main__':
    test()
    #with open(sys.argv[1]) as f:
        #print(parse(f.read()))
