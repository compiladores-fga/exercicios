# Cfg-list

## Q1
### Q1.1 JSON

```
r"""
    ?start: element*

    ?element : STRING
        |   NUMBER
        |   object
        |   list
        |   "true"
        |   "false"
        |   "null"

    object : "{" (STRING ":" element ("," STRING ":" element)*)? "}"
    list  : "[" (element ("," element)*)? "]"
    STRING : /"([^"\\\n\r\b\f]+|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*"/
    NUMBER : /-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?/

    %ignore /\s+/
"""
```

### Q1.2 LISP

```
r"""
    ?start : value+

    ?value : list
        | element
        | "'" value+ -> quote

    ?list: "(" value* ")"

    ?element : STRING -> string
        | NUMBER -> number
        | BOOL -> boolean
        | CHAR -> char
        | SYMBOL -> symbol
        | NAME -> name


    STRING : /"[^"\\]*(\\[^\n\t\r\f][^"\\]*)*"/
    NUMBER : /-?(0|[1-9]+)(\.\d+)?/
    NAME   : /([a-zA-Z]+[\-\_]?)+\??/
    BOOL   : /(#t|#f)/
    CHAR   : /#\\\w+/
    SYMBOL : /[-+.*\/<=>!?$%_&~^@]+/

    %ignore /\s+/
    %ignore /;[^\n]*/
"""
```

### Q1.3 LISP-II

```
r"""
    ?start : value+

    ?value : list
        | element
        | "'" value+ -> quote

    ?list: "(" (value ","?)* ")"

    ?element : STRING -> string
        | NUMBER -> number
        | BOOL -> boolean
        | CHAR -> char
        | SYMBOL -> symbol
        | NAME -> name


    STRING : /"[^"\\]*(\\[^\n\t\r\f][^"\\]*)*"/
    NUMBER : /-?(0|[1-9]+)(\.\d+)?/
    NAME   : /([a-zA-Z]+[\-\_]?)+\??/
    BOOL   : /(#t|#f)/
    CHAR   : /#\\\w+/
    SYMBOL : /[-+.*\/<=>!?$%_&~^@]+/

    %ignore /\s+/
    %ignore /;[^\n]*/
"""
```

### Q1.4 Python

```
r"""
    ?start: element*

    ?element : STRING
        |   NUMBER
        |   object
        |   list
        |   BOOL
        |   "null"

    object : "{" (STRING ":" element ("," STRING ":" element)*)? "}"
    list   : "[" (element ("," element)* ","?)? "]"

    STRING : /"[^\n"\\]*(?:\\.[^\n"\\]*)*"/
    NUMBER : /-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?/
    BOOL   : /(True|False)/

    %ignore /\s+/
"""
```

### Q1.5 JSON

```
r"""
    ?start: element*

    ?element : STRING
        |   NUMBER
        |   object
        |   list
        |   "true"
        |   "false"
        |   "null"

    object : "{" (STRING ":" element ("," STRING ":" element)*)? "}"
    list   : "[" (element (","+ element)* ","*)? "]"
    STRING : /"([^"\\\n\r\b\f]+|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*"/
    NUMBER : /-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?/

    %ignore /\s+/
"""
```

## Q2
