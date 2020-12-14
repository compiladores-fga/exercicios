## Q1

### 1. JSON: usa "[]" como delimitadores e exige uma vírgula entre cada elemento da lista

```
r"""
    start   :  json

    json    :   "["( elem ",")* elem "]"

    elem    : NUMBER
            | STRING

    NUMBER  : /-?\d+(\.\d+)?/
    STRING  : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 2. LISP: usa "()" como delimitadores e não utiliza vírgulas para separar os elementos.

```
r"""
    start   :   lisp

    lisp    :   "(" elem* ")"

    elem    : NUMBER
            | STRING

    NUMBER  : /-?\d+(\.\d+)?/
    STRING  : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 3. LISP-II: em algumas versões de LISP, a vírgula é opcional, também podendo aparecer após o último elemento.

```
r"""
    start   :   lispII

    lispII  :   "(" (elem ","?)* ")"

    elem    : NUMBER
            | STRING

    NUMBER  : /-?\d+(\.\d+)?/
    STRING  : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 4. Python: similar ao JSON, mas permite uma vírgula após o último elemento. `[,]` é inválido.

```
r"""
    start   :   python

    python  :   "["( elem ",")* (elem "," | elem)"]"

    elem    : NUMBER
            | STRING

    NUMBER  : /-?\d+(\.\d+)?/
    STRING  : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```

### 5. Javascript: similar ao JSON, mas aceita **1 ou mais** vírgulas entre os elementos e após o último elemento. `[,]`, assim como `[1,2,,3,,,]` são valores válidos. Em Javascript, o espaço vazio entre duas vírgulas é interpretado como um elemento `undefined`.

```
r"""
    start       :   javascript

    javascript  :   "[" (elem ",")* ((elem ",")|elem) "]"

    elem        : NUMBER -> number
                | STRING -> string
                |        -> undefined

    NUMBER      : /-?\d+(\.\d+)?/
    STRING      : /"[^"\\]*"/
    %ignore /\s+/
    %ignore /\#.*/
"""
```