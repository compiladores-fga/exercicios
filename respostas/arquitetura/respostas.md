## parser-fmt

### Q1

```python
"""
Simple JSON Parser
==================

The code is short and clear, and outperforms every other parser (that's written in Python).
For an explanation, check out the JSON parser tutorial at /docs/json_tutorial.md
"""
import sys
import math
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
            "empty_object" : {}, // comentário
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

    j = parse(test_json)
    print(j)
    # import json
    # assert j == json.loads(test_json)


if __name__ == '__main__':
    test()
    # with open(sys.argv[1]) as f:
    #     print(parse(f.read()))
```

## comp-vs-interp

### Q1

- Resposta:

O interpretador realiza a análise léxica, sintática e semântica da primeira instrução do código fonte, realiza sua conversão em linguagem de máquina e ordena a execução da instrução e após isso o interpretador repete esse processo até a última instrução do código fonte. Caso esse programa for executado pela segunda vez o interpretador realizará novamente as análises sintáticas  e léxicas pois os comandos em linguagem de máquina não ficam salvos para futuras  execuções. <br>
O compilador assim como o interpretador realiza a análise léxica, sintática e semântica do código, porém o compilador faz isso de uma maneira diferente em que se recebe a primeira instrução do código fonte e a converte linguagem de máquina, realizamdp esse processo até a última instrução do código fonte. Caso todas as instruções tenham sido convertidas para linguagem de máquina sem a ocorrência de erros, o compilador retorna para a primeira instrução - já convertida em linguagem de máquina - realizando a sua execução e repete esse processo para todas as instruções do código fonte, salvando essas instruções em um novo programa executável. Caso o programa seja executado por uma segunda vez não será necessário realiar todo esse processo, pois as intruções em linguagem de máquina foram salvas em um arquivo executável.

### Q2

- Resposta:

Interpretador c: https://github.com/jpoirier/picoc
Compilador python: https://github.com/Nuitka/Nuitka