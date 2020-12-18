## [cfg-cst]: Relacionar gramática com a representação do código como árvore concreta 

**Q1)** 

1. 42
2. 2 * (11 + 2 * 5)

```
expr : expr "+" term
     | term

term : term "*" atom
     | atom

atom : NUMBER
     | "(" expr ")"

NUMBER : /\d+/
```

```

src:  42  TREE:  Tree('start', [Tree('number', [Token('NUMBER', '42')])])
Expressão:
42
Pretty:  start
  number        42
  
  
src:  2 * (11 + 2 * 5)  
TREE:  Tree('start', [Tree('pow', [Tree('number', [Token('NUMBER', '2')]), Tree('listing', [Tree('soma', [Tree('number', [Token('NUMBER', '11')]), Tree('pow', [Tree('number', [Token('NUMBER', '2')]), Tree('number', [Token('NUMBER', '5')])])])])])])

                                   Expressão: 2 * (11 + 2 * 5) -> ['*', 2, [['+', 11, ['*', 2, 5]]]]
                                   /         |              \
                                  /          |                \
                                 /           |                  \
                                '*'          2                   ['+', 11, ['*', 2, 5]]
                                                                 /         |      \
                                                                /          |       \
                                                               /           |        \
                                                              '+'          11       ['*', 2, 5] 
                                                                                     /  |   \
                                                                                    /   |    \
                                                                                   /    |     \
                                                                                  '+'   2      5        

Pretty:  start
  pow
    number      2
    listing
      soma
        number  11
        pow
          number        2
          number        5                                                            

```
