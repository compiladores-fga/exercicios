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
          | INF                -> inf
          | "NaN"              -> nan

    array  : "[" [value ("," value)* ","?] "]"
    object : "{" [pair ("," pair)* ","?] "}"
    pair   : string ":" value
    string : ESCAPED_STRING
        |    /[a-zA-Z_]+/ -> custom_string

    INF    : /-?Infinity/

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    %ignore /\/\/[^\n]*/
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def custom_string(self, s):
        return s

    def inf(self, tk):
        if tk[0] == '-':
            return -float('inf')
        return float('inf')

    def nan(self, tk):
        return float('nan')


    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

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
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
            "nothing"      : null,

            "comment"      : true, // comentário ok
            "virg_list"    : [1, 2, 3, 4,],
            "virg_obj"     : {"obj": true,},
            "string"       : string_sem_aspa,
            "inf"          : Infinity,
            "-inf"          : -Infinity,
            "nan"          : NaN,
        }
    '''

    j = parse(test_json)
    print(j)


test()

# exemplo = r"""
# {
#     "teste_comentario" : "teste", // comentário
#     "teste_lista": [1, 2, 3,], // lista com vírgula no final
#     "teste_objeto": {"obj": true,}, // objeto com vírgula no final
#     "teste_string": minha_string, // testando string sem aspas
# }
# """


# tree = grammar.parse(exemplo)
# print(tree)
