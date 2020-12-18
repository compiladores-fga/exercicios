## [nfa-thompson]: Criação de NFA para representação de Regex na construção de Thompson

**Q1)** Utilize a construção de Thompson para criar um NFA-ε para as seguintes expressões regulares.

1. `ab|c`

<img src="/imagens/imagens_automatos/nfa-thompson-1.png" width="800">



2. `ab(cd|ε)`

<img src="/imagens/imagens_automatos/nfa-thompson-2.png" width="800">

3. `a*b*`

<img src="/imagens/imagens_automatos/nfa-thompson-3.png" width="800">


4. `a(b|c)d`

<img src="/imagens/imagens_automatos/nfa-thompson-4.png" width="800">


5. `b(a|b)*a|a`
```
Considerando o entendimento como: b(a|b)*(a|a)
```

<img src="/imagens/imagens_automatos/nfa-thompson-5_a_2.png" width="800">

```
Considerando o entendimento como: (b(a|b)*a)|(a)
```

<img src="/imagens/imagens_automatos/nfa-thompson-5_b.png" width="800">
