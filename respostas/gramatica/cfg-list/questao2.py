from lark import Lark, InlineTransformer, Token

# **Q2)** Crie um programa baseado no último exemplo da questão anterior que leia listas no estilo Javascript e retorne o valor processado, trocando `undefined` por None em Python. Assuma que os elementos podem ser outras listas ou números inteiros. Deste modo, o código de entrada `"[1,,2,[,,],]"` seria convertido em `[1, None, 2, [None, None]]`.
q2 = r"""
    start : list
    list  : "[" (item | ",")* "]"
    item  : ([1-9] | [a-z])+
"""

grammar = Lark(q2)


# for example in examples:
#   result = grammar.parse(example)
#   print(result.pretty())


class tr(InlineTransformer):
  def array(self, *arg):
    return list(arg)

  def number(self, arg):
    return int(arg)

  def empty(self):
    return None


def do():
  tra = tr()
  examples = ["[1,,2,[,,],]"]
  tree = grammar.parse(examples)

  print(tra.transform(tree))

do()
