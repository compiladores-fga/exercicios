from lark import Lark

expressions = [
  "[10,50,600,700]",
  "(10 50 600 700)",
  "(10, 50, 600, 700)",
  "[10, 50, 600, 700,]",
  "[10, 50, 600, 700,,,,]",
]

for expression in expressions:
  grammar = Lark(open("json.lark"))
  tree = grammar.parse(expression)
  print(tree.pretty())
