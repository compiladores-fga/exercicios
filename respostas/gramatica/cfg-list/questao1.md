Referência: https://bnfplayground.pauliankline.com/

# **Q1)** Monte uma gramática BNF ou EBNF para identificar listas de elementos em cada um dos casos abaixo:

# 1. JSON: usa "[]" como delimitadores e exige uma vírgula entre cada elemento da lista
```
    <start> ::= <list>
    <list>  ::= "[" <item> ("," <item>)* "]"
    <item>  ::= ([1-9] | [a-z])+
```

# 2. LISP: usa "()" como delimitadores e não utiliza vírgulas para separar os elementos.
```
    <start> ::= <list>
    <list>  ::= "(" <item> (" "+ <item>)* ")"
    <item>  ::= ([1-9] | [a-z])+
```

# 3. LISP-II: em algumas versões de LISP, a vírgula é opcional, também podendo aparecer após o último elemento.
```
    <start> ::= <list>
    <list>  ::= "(" (" ")* <item> (" ")* (",")? (" ")* ((<item>) (" ")* (",")? (" ")*)* ")"
    <item>  ::= ([1-9] | [a-z])+
```
# 4. Python: similar ao JSON, mas permite uma vírgula após o último elemento. `[,]` é inválido.
```
    <start> ::= <list>
    <list>  ::= "[" <item> ("," <item>)* (",")? "]"
    <item>  ::= ([1-9] | [a-z])+
```

# 5. Javascript: similar ao JSON, mas aceita **1 ou mais** vírgulas entre os elementos e após o último elemento. `[,]`, assim como `[1,2,,3,,,]` são valores válidos. Em Javascript, o espaço vazio entre duas vírgulas é interpretado como um elemento `undefined`.
```
    <start> ::= <list>
    <list>  ::= "[" (<item> | ",")* "]"
    <item>  ::= ([1-9] | [a-z])+
```