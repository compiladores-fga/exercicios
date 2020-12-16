### Q1

#### G1
1.  S ⟶ a S b
2.  S ⟶ ε

- - - - | a | b | $ 
---     | - | - | - 
   S    | 1 | 2 | 2 

First(S) = {a, ε}

Follow(S) = {b, $}

#### G2
1.  S ⟶ E S
2.  S ⟶ ε
3.  E ⟶ v
4.  E ⟶ ( L )
5.  L ⟶ E L
6.  L ⟶ ε

Gramática não compatível com LL(1) por possuir ambiguidade em suas regras e os conjuntos "First" não são disjuntos.

#### G3
1.  S ⟶ E
2.  S ⟶ ε
3.  E ⟶ v
4.  E ⟶ λ v . E
5.  E ⟶ ( E R )
6.  E ⟶ let v = E in E
7.  R ⟶ E
8.  R ⟶ ε

Gramática não compatível com LL(1) por possuir ambiguidade em suas regras e os conjuntos "First" não são disjuntos.