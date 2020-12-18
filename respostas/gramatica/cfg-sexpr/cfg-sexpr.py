
import re
import math
from lark import Lark, InlineTransformer


grammar = Lark(r"""
  ?start: expr

  ?expr: expr "+" term   -> add
       | term

  ?term: term "*" atom   -> mult
       | atom

  ?atom: NUMBER          -> number
       | "(" expr ")"

  NUMBER : /\d+/

  %ignore /\s+/
  %ignore /\#.*/
"""
)


class Transformer(InlineTransformer):
  def add(self, token, token2):
    return ["+", token, token2]
  
  def mult(self, token, token2):
    return ["*", token, token2]
  
  def number(self, token):
    try:
      return int(token)
    except:
      return float(token)