from lark import Lark, InlineTransformer, Token

grammar = Lark(
r"""
    ?start: expr 
    
    ?expr : expr "+" term -> add
        | term
        
    ?term : term "*" atom -> mul
        | atom
        
    ?atom : NUMBER -> number
        | "(" expr ")"
        
    NUMBER : /\d+/
    
    %ignore /\s+/
    %ignore /\#.*/
"""
)

class Transformer(InlineTransformer):
    def add(self, token1, token2):
        return ["+", token1, token2]

    def mul(self, token1, token2):
        return ["*", token1, token2]
    
    def number(self, token):
        try:
            return float(token)            
        except:
            return int(token)