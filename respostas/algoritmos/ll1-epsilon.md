## [ll1-epsilon]: Tratar caso especial do LL(1) em gramática que possui epsilons

## G1
```
1.  S ⟶ a S b
2.  S ⟶ ε
```

||a|b|$|
| :---: | :---: | :---: | :---: |
|S|1|2|2|

First(S) = {a, ε} Follow(S) = {b, $}

## G2
```
1.  S ⟶ E S
2.  S ⟶ ε
3.  E ⟶ v
4.  E ⟶ ( L )
5.  L ⟶ E L
6.  L ⟶ ε
```

Possuir ambiguidade e os conjuntos "First" não disjuntos.


## G3
```
1.  S ⟶ E
2.  S ⟶ ε
3.  E ⟶ v
4.  E ⟶ λ v . E
5.  E ⟶ ( E R )
6.  E ⟶ let v = E in E
7.  R ⟶ E
8.  R ⟶ ε
```

Possuir ambiguidade e os conjuntos "First" não disjuntos.
