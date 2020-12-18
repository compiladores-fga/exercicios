Autômatos
=========

## [dfa-repr]: Entender o mecanismo de operação de um autônomo determinístico finito

**Q1)**
1. Sequências de a's e b's em que os a's aparecem em pares. Ex.: aa, baab, bbb, aaaab

<img src="/imagens/imagens_automatos/1_a.png" width="800">


| f(estado) | a | b |
| :---: | :---: | :---: |
|  q0 |  q1 | q0 |
|  q1 |  q0 | q2 |
|  q2 |  q2 | q2 |
|
```
**Ex: aa:** q0(Estado inicial) -> q1 -> q0(Estado final)

```
2. Sequências de a's e b's com um número par de a's. Ex.: aa, abba, abaabbba

<img src="/imagens/imagens_automatos/1_b.png" width="800">

| f(estado) | a | b |
| :---: | :---: | :---: |
|  q0 |  q1 | q0 |
|  q1 |  q0 | q1 |
|
```
**Ex: aa:** q0(Estado inicial) -> q1 -> q0(Estado final)
```
3. Sequências de a's e b's que contenham pelo menos uma ocorrência de cada letra.


<img src="/imagens/imagens_automatos/1_c.png" width="800">



| f(estado) | a | b |
| :---: | :---: | :---: |
|  q0 |  q1 | q3 |
|  q1 |  q1 | q2 |
|  q2 |  q2 | q2 |
|  q3 |  q2 | q3 |
|
```
**Ex: ab:** q0(Estado inicial) -> q1 -> q2(Estado final)

```
Resolva 1 exemplo para demonstrar competência.
