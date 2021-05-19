## Q1

### 1

Json
```
?start  :   list
?list   :   "[" elem ("," elem)* "]"
```

### 2

Lisp
```
?start  :   list
?list   :   "(" elem+ ")"
```

### 3

Lispii
```
?start  :   list
?list   :  "(" (elem ","?)+ ")"
```

### 4

Python
```
?start  :   list
?list   :   "[" (elem ",")+ "]"
```
### 5

Js
```
?start  :   list
?list   :   "[" (elem? ","+)+ "]"
```