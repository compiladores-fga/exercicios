import sys

from lark import Lark, Transformer, v_args

json_grammar = r"""
	?start: value
	?value: object
		| array
		| STRING			 -> string
		| SIGNED_NUMBER      -> number
		| "true"             -> true
		| "false"            -> false
		| "null"             -> null
		| "Infinity"		 -> infinity
		| "-" WS* "Infinity"		 -> ninfinity
		| "NaN"				 -> nan
	array  : "[" [value ("," value)* ","?] "]"
	object : "{" [pair ("," pair)* ","?] "}"
	pair   : STRING ":" value
	STRING : /("([^"\\\n\r\b\f]+|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*")|([a-zA-Z_]+)/
	%import common.ESCAPED_STRING
	%import common.SIGNED_NUMBER
	%import common.WS
	%ignore WS
	%ignore /\/\/.*/
"""


class TreeToJson(Transformer):
	@v_args(inline=True)
	def string(self, s):
		return s

	def infinity(self,token):
		return float("inf")

	def ninfinity(self,token):
		return -float("inf")

	def nan(self,token):
		return float("nan")
		

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
			"booleans"     : { "YES" : true, "NO" : false, aa :- Infinity ,},
			"numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ,Infinity, NaN,],
			"STRINGs"      : [ This , [ "And" , "That", "And a \\"b" ] ],
		//	"nothing"      : null
		}
	'''

	j = parse(test_json)
	print(j)
	# import json
	# assert j == json.loads(test_json)


if __name__ == '__main__':
	test()
	# with open(sys.argv[1]) as f:
	# 	print(parse(f.read()))