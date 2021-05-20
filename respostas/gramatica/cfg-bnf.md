Referência: https://bnfplayground.pauliankline.com/

# Expresse as linguagens abaixo em notação BNF (não utilize os operadores extendidos (*, +, [], ?, ()))

# 1. Uma ou mais ocorrências de a. Ex.: `a, aaa, aaaaaaa`
```
    <start> ::= <a>
    <a> ::= "a" | "a" <a>
```



# 2. Strings que começam com a, seguem com uma ou mais ocorrências de b ou c e terminam com d. Ex.: `ad, abcd, abbbd`
```
    <start> ::= <lets> <d>
    <let> ::= "a" | "b" | "c"
    <lets> ::= <let> | <let> <lets>
    <d> ::= "d"
```



# 3. Números positivos com parte decimal opcional. Ex.: `0, 42, 3.14`
```
    <start> ::= <nums> <dec> | <nums>
    <num> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    <nums> ::= <num> | <num> <nums>
    <dec> ::= "." <nums>
```

