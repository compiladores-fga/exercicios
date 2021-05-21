Referência: https://bnfplayground.pauliankline.com/

# Converta as expressões em EBNF para BNF assumindo que os símbolos terminais e não-terminais utilizados estão definidos adequadamente fora da regra em questão.

# 1. `imp : "from" name "import" (VAR [as VAR])+`
```
    imp  : "from" name "import" vars
    vars :  VAR | VAR as VAR | vars vars
```

# 2. `seq : "(" (a | b)* ")"`
```
    seq : "(" ")" | "(" in ")"
    in  : a | b
```

# `lst : "{" [key ":" exp ("," key ":" exp)* ","?] "}"`
```
    lst : "{" in "}" | "{" "}"
    in  : key ":" exp lel | key ":" exp lel "," | key ":" exp | key ":" exp ","
    lel : "," key ":" exp | lel lel
```
