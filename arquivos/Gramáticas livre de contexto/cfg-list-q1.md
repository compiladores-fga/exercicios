## Q1) Monte uma gramática BNF ou EBNF para identificar listas de elementos em cada um dos casos abaixo:

#### 1. JSON
'''

    gramatica ::= '[' items (',' items)* ']'
    items ::= '0' | '1' | '2' | '3' | '4'
 | '5' | '6' | '7' | '8' | '9'

'''

#### 2. LISP
'''

    gramatica ::= '(' items items* ')'
    items ::= '0' | '1' | '2' | '3' | '4'
 | '5' | '6' | '7' | '8' | '9'

'''

#### 3. LISP-II
'''

    gramatica ::= '(' items (','? items)* ','? ')'
    items ::= '0' | '1' | '2' | '3' | '4'
 | '5' | '6' | '7' | '8' | '9'

'''

#### 4. Python
'''

    gramatica ::= '[' items (',' items)* ','? ']'
    items ::= '0' | '1' | '2' | '3' | '4'
 | '5' | '6' | '7' | '8' | '9'

'''

#### 5. Javascript
'''

    gramatica ::= '[' items (',' items?)* ','? ']'
    items ::= '0' | '1' | '2' | '3' | '4'
 | '5' | '6' | '7' | '8' | '9'

'''