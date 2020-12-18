## [nfa-dfa]: Conversão de NFA para DFA

**Q1)** 


```
Transformação 'A':

O estado inicial é equivalente a: A -> A,B,C

f({A, B, C},a) = {D}
f({A, B, C},b) = {E}
f({D},a) = {}
f({D},b) = {E}
f({E},a) = {C}
f({E},b) = {}
```


<img src="/imagens/imagens_automatos/nfa-dfa_a_conv.png" width="800">

```
Transformação 'B':

O estado inicial é equivalente a: A -> A,B,D

f({A, B, D},a) = {B, C, D}
f({B, C, D},a) = {B, C, D}
```

<img src="/imagens/imagens_automatos/nfa-dfa_b_conv_2.png" width="800">
