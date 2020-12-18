## [ll1-conv]: Criação da tabela de transição para o algoritmo LL(1)

## G1
```
1.  S ⟶ a
2.  S ⟶ ( S )
3.  S ⟶ S *
4.  S ⟶ S S
5.  S ⟶ S | S
```
* Em dado momento é impossivel distinguir-se de algumas regras pois possui ambiguidade.

## G2
```
1.  S ⟶ + S S
2.  S ⟶ * S S
3.  S ⟶ ~ S
4.  S ⟶ n
```
Gramática compatível.


||+|*|~|n|$|
| :---: | :---: | :---: | :---: | :---: | :--- |
|S|1|2|3|4||

first = {+,*,~,n} Follow = {$}


## G3
```
1.  S ⟶ S + S
2.  S ⟶ S * S
3.  S ⟶ - S
4.  S ⟶ ( S )
5.  S ⟶ n
```
Gramática compatível.


