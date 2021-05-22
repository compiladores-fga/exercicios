## [cfg-bnf]: Entender e reconhecer operações básicas de gramática generativa na notação BNF

Expresse as linguagens abaixo em notação BNF (não utilize os operadores extendidos (*, +, [], ?, ()))

1. Uma ou mais ocorrências de a. Ex.: `a, aaa, aaaaaaa`

```
<a> ::= "a" | "a" <a>
```

2. Strings que começam com a, seguem com uma ou mais ocorrências de b ou c e terminam com d. Ex.: `ad, abcd, abbbd`

```
<start> ::= "a" <b> | <c> "d"
<b> ::= "b" | "b" <b> | <c>
<c> ::= "c" | "c" <c> | <b>
```

3. Números positivos com parte decimal opcional. Ex.: `0, 42, 3.14`

```
<start> ::= <number> | <number> "." <number>
<number> ::= <digit> | <digit> <number>
<digit> :: = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```