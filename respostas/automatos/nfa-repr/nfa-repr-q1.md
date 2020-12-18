## [nfa-repr]: Entender o mecanismo de operação de um autônomo não-determinístico finito

Resolva as duas questões para demonstrar competência.

**Q1)** O autômato abaixo representa uma linguagem que aceita números inteiros ou números com parte decimal. 

1. O que faz com que o autômato seja classificado como um NFA e não um DFA?<br>
O estado A possui duas possíveis transições.<br><br>
2. Mostre o conjunto de estados que o autômato percorre para analisar as strings: a) `42` b) `3.14` c) `123.` e diga em cada caso se a string foi aceita ou não. <br>
a) `42` -> Aceito<br>

| char | transição |
| :-------:| :-----------: |
| 4 | A->B |
| 2 | B->B |
<br>

b) `3.14` -> Aceito<br>

| char | transição |
| :-------:| :-----------: |
| 3 | A->C |
| . | C->D |
| 1 | D->E |
| 4 | E->E |
<br>

b) `123` -> Rejeitado<br>

| char | transição |
| :-------:| :-----------: |
| 1 | A->C |
| 2 | C->C |
| 3 | C->C |
| . | C->D |
<br><br>

3. Proponha uma mudança simples para transformá-lo em um DFA sem alterar a linguagem que ele representa.<br>
Retirar o estado B e tornar o estado C terminal
