## Q1

### 1
```
r"""
    start: json

    json: "["( elem ",")* elem "]"

    elem: NUMBER
        | STRING

    NUMBER : /-?\d+(\.\d+)?/
    STRING : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 2

```
r"""
    start: lisp

    lisp: "(" elem* ")"

    elem: NUMBER
        | STRING

    NUMBER : /-?\d+(\.\d+)?/
    STRING : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 3

```
r"""
    start: lisp2

    lisp2: "(" (elem ","?)* ")"

    elem: NUMBER
        | STRING

    NUMBER : /-?\d+(\.\d+)?/
    STRING : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 4

```
r"""
    start: python

    python: "["( elem ",")* (elem "," | elem)"]"

    elem: NUMBER
        | STRING

    NUMBER : /-?\d+(\.\d+)?/
    STRING : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 5

```
r"""
    start: javascript

    javascript: "[" (elem ",")* ((elem ",")|elem) "]"

    elem: NUMBER -> number
        | STRING -> string
        |      -> undefined

    NUMBER : /-?\d+(\.\d+)?/
    STRING : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```
