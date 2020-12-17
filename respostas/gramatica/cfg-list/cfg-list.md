## Q1

### 1

```
r"""
?start  :   list
?list   :   "[" elem ("," elem)* "]"    -> json
"""
```

### 2
```
r"""
?start  :   list
?list   :   "(" elem+ ")"   -> lisp
"""
```

### 3

```
r"""
?start  :   list
?list   :  "(" (elem ","?)+ ")"    -> lispii
"""
```

### 4

```
r"""
?start  :   list
?list   :   "[" (elem ",")+ "]"   -> python
"""
```
### 5
```
r"""
?start  :   list
?list   :   "[" (elem? ","+)+ "]"    -> js
"""
```