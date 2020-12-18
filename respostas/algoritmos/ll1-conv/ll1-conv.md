## [ll1-conv]: Criação da tabela de transição para o algoritmo LL(1)

**Q1)** Verifique se as gramáticas abaixo são compatíveis com o LL(1) e monte a tabela de transição para as gramáticas compatíveis. Em caso contrário, aponte o motivo do conflito da gramática com o LL(1). Resolva 1 exemplo de gramática compatível com LL(1) para demonstrar competência.

## G1
```
1.  S ⟶ a
2.  S ⟶ ( S )
3.  S ⟶ S *
4.  S ⟶ S S
5.  S ⟶ S | S
```
Gramática incompatível por existir ambiguidade nas suas regras.<br><br>

## G2
```
1.  S ⟶ + S S
2.  S ⟶ * S S
3.  S ⟶ ~ S
4.  S ⟶ n
```

|  | + | * | ~ | n | $ |
| :----: | :---: | :---: | :---: | :---: | :---: |
| S | 1 | 2 | 3 | 4 | |

First(S) = {+, *, ~, n}<br><br>
## G3
```
1.  S ⟶ S + S
2.  S ⟶ S * S
3.  S ⟶ - S
4.  S ⟶ ( S )
5.  S ⟶ n
```
Gramática compatível.