## [cfg-ebnf]: Entender operadores na notação EBNF

Converta as expressões em EBNF para BNF assumindo que os símbolos terminais e não-terminais utilizados estão definidos adequadamente fora da regra em questão.

1. `imp : "from" name "import" (VAR [as VAR])+`

```
<imp> ::= "from" <name> "import" <lib>
<lib> ::= <var> | <var> <as> <var> | <var> <lib> | <var> <as> <var> <lib>
```

2. `seq : "(" (a | b)* ")"`

```
<seq> ::= "(" <arg> ")"
<arg> ::= <a> <arg> | <b> <arg> | E 
```

3. `lst : "{" [key ":" exp ("," key ":" exp)* ","?] "}"`

```
<lst> ::= "{" <expr> "}"
<expr> ::= <key> ":" <exp> <trem> | <key> ":" <exp> <trem> "," | E
<trem> ::= "," <key> ":" <exp> <trem> | E
```