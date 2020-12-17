## [ll1-conv]

## G1
```
1.  S ⟶ a
2.  S ⟶ ( S )
3.  S ⟶ S *
4.  S ⟶ S S
5.  S ⟶ S | S
```
**R:** Gramática incompatível com LL(1) devido ambiguidade nas regras 

## G2
```
1.  S ⟶ + S S
2.  S ⟶ * S S
3.  S ⟶ ~ S
4.  S ⟶ n
```

**Tabela de transição:**

&nbsp; | + | * | ~ | n | $ 
--- | - | - | - | - | - 
 S  | 1 | 2 | 3 | 4 | 
 
**R:** First(S) = {+, *, ~, n}

## G3
```
1.  S ⟶ S + S
2.  S ⟶ S * S
3.  S ⟶ - S
4.  S ⟶ ( S )
5.  S ⟶ n
```
**R:** Gramática compatível
