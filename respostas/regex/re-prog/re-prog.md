# Questões re-prog
## Modelo de resposta: *expressão a converter* -> *expressão convertida*
## 1
```r"[a-c]" -> (a|b|c)*```
## 2
```r"[ab]+" -> (a|b)(a|b)*```
## 3
```r"a?b?c?" -> (a|)(b|)(c|)```
## 4
```r"[abde]|ab|c?" -> (a|b|d|e)|ab|(c|)```