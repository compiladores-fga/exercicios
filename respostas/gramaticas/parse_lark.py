from lark import Lark
parser = Lark(r"""
    start: expr
    expr: NUMBER | call
    call: OPERATOR expr expr
    OPERATOR: /[+-\/*]/
    NUMBER: /\d+/
    %import common.WS
    %ignore WS
""")

if __name__ == '__main__':

    line =r"""
    + * 10 20 30 
    """

    print(line)

    response = parser.parse(line)
    print(response)

    print(response.pretty())
