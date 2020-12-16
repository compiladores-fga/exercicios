### Q1

#### G1

Gramática não compatível com LL(1) por possuir recursividade e ambiguidade em suas regras.


#### G2
1.  S ⟶ + S S
2.  S ⟶ * S S
3.  S ⟶ ~ S
4.  S ⟶ n

- - - - | + | * | ~ | n | $ 
---     | - | - | - | - | - 
   S    | 1 | 2 | 3 | 4 | 

First(S) = {+,*,~,n}

Follow(S) = {$}

#### G3

Gramática compatível com LL(1).