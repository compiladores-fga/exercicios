## [ll1-epsilon]: Tratar caso especial do LL(1) em gramática que possui epsilons

**Q1)** Verifique se as gramáticas abaixo são compatíveis com o LL(1) e monte a tabela de transição para as gramáticas compatíveis. Em caso contrário, aponte o motivo do conflito da gramática com o LL(1). Resolva 1 exemplo de gramática compatível com LL(1) para demonstrar competência.

## G1
```
1.  S ⟶ a S b
2.  S ⟶ ε
```
|  | a | b | $ |
| :----: | :---: | :---: | :---: |
| S | 1 | 2 | 2 |

First(S) = {a, ε}<br>
Follow(S) = {b, $}<br><br>


## G2
```
1.  S ⟶ E S
2.  S ⟶ ε
3.  E ⟶ v
4.  E ⟶ ( L )
5.  L ⟶ E L
6.  L ⟶ ε
```
Gramática incompatível por possuir ambiguidade em suas regras, os conjuntos First não são disjuntos.<br><br>

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
Gramática incompatível por possuir ambiguidade em suas regras, os conjuntos First não são disjuntos.