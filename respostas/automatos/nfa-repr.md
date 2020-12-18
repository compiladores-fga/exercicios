## [nfa-repr]: Entender o mecanismo de operação de um autônomo não-determinístico finito

Resolva as duas questões para demonstrar competência.

**Q1)** 

1. 


Na saida do estado 'A' serão percorrido paralelamente os estados 'B' e 'C'.

2. 
```
42 - CAMINHO: AB -> Aceito "No caminho paralelo não é aceito."
3.14 - CAMINHO: ACDE -> Aceito "No caminho paralelo não é aceito."
123. - NÃO ACEITO, é necessario que se tenha ao menos um algarismo apos o ponto.
```
<img src="/imagens/imagens_automatos/nfa-repr-2.png" width="800">

3. 

O estado 'B' torna-se desnecessario quando 'C' é adicionado ao o conjunto de estados de aceite. Com essa alteração passa-se a exixtir um unico caminho.

<img src="/imagens/imagens_automatos/nfa-repr-3.png" width="800">

**Q2)** 

1. 

<img src="/imagens/imagens_automatos/nfa-repr-Q2.png" width="800">

* Ex: a{12}:** A(Estado inicial) -> B -> C -> B(Estado final)

2. 

<img src="/imagens/imagens_automatos/nfa-repr-Q2_B.png" width="800">


* Ex: a{13}:** A(Estado inicial) -> B -> C(Estado final)


Resolva 1 dos exemplos acima para resolver a questão.
