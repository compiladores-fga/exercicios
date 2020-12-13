# CFG_LIST

## Q1

### JSON

```
r"""
    start: expr

    expr : "[" elem (elem "," )* "]"

    elem: NUMBER
        | NAME

    NUMBER : /-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/
    NAME   : /\w+/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### LISP

```
r"""
    start: elem

    expr : "(" elem* ")"

    elem: NUMBER
        | NAME

    NUMBER : /-?(?:0|[1-9]\d*)(?:\.\d+)?/
    NAME   : /\w+/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### LISP-II

```
r"""
    start: elem
    expr : "(" (elem ","?)* ")"

    elem: NUMBER
        | NAME

    NUMBER : /-?(?:0|[1-9]\d*)(?:\.\d+)?/
    NAME   : /\w+/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### Python

```
r"""
    start: elem
    expr : "["( elem ",")* (elem "," | elem)"]""

    elem: NUMBER
        | NAME

    NUMBER : /-?(?:0|[1-9]\d*)(?:\.\d+)?/
    NAME   : /\w+/
    %ignore /\s+/
    %ignore /\#.*/
```

### Javascript

```
r"""
    start: elem
    expr : "[" (elem ",")* ((elem ",")|elem) "]"

    elem: NUMBER    -> number
        | NAME      -> name
        |           -> undefined

    NUMBER : /-?(?:0|[1-9]\d*)(?:\.\d+)?/
    NAME   : /\w+/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

## Q2

```
r"""
    start: elem
    expr : "[" (elem ",")* ((elem ",")|elem) "]"

    elem: NUMBER    -> number
        | NAME      -> name
        |           -> undefined

    NUMBER : /-?(?:0|[1-9]\d*)(?:\.\d+)?/
    NAME   : /\w+/
    %ignore /\s+/
    %ignore /\#.*/
"""
```