Autômatos
=========

## [dfa-repr]: Entender o mecanismo de operação de um autônomo determinístico finito

**Q1)** Crie um autômato determinístico finito equivalente às linguagens abaixo. Em cada caso, faça um diagrama de operação do autômato, enfatizando as transições, estado inicial e estados de aceite e monte separadamente a tabela de transição. 

1. Sequências de a's e b's em que os a's aparecem em pares. Ex.: aa, baab, bbb, aaaab
2. Sequências de a's e b's com um número par de a's. Ex.: aa, abba, abaabbba
3. Sequências de a's e b's que contenham pelo menos uma ocorrência de cada letra.

Resolva 1 exemplo para demonstrar competência.


## [dfa-prog]: Implementar um algoritmo para a execução de autômatos determinísticos finitos em linguagem de programação

Resolva as duas questões para demonstrar competência.

**Q1)** Crie um programa que peça uma string de entrada para o usuário, execute o autômato determinístico finito abaixo, verifique se a string é aceita ou não pelo autômato e imprima `Aceito` ou `Rejeitado` de acordo com o resultado.

![Diagrama](./arquivos/dfa-prog-q1.svg)

**Q2)** Modifique uma cópia do programa da seção anterior em que o estado inicial seja B e o conjunto de estados de aceite seja {C}.


## [nfa-repr]: Entender o mecanismo de operação de um autônomo não-determinístico finito

Resolva as duas questões para demonstrar competência..

**Q1)** O autômato abaixo representa uma linguagem que aceita números inteiros ou números com parte decimal. 

![Diagrama](./arquivos/nfa-repr-q1.svg)

1. O que faz com que o autômato seja classificado como um NFA e não um DFA?
2. Mostre o conjunto de estados que o autômato percorre para analisar as strings: a) `42` b) `3.14` c) `123.` e diga em cada caso se a string foi aceita ou não. 
3. Proponha uma mudança simples para transformá-lo em um DFA sem alterar a linguagem que ele representa.

**Q2)** Crie um autômato não-determinístico finito equivalente às linguagens abaixo. Em cada caso, faça um diagrama de operação do autômato, enfatizando as transições, estado inicial e estados de aceite e monte separadamente a tabela de transição. 

1. Sequências de n a's, onde n é um múltiplo de 3 ou 5. Ex.: a{12}, onde 12 = 3 x 4
2. Sequências de n a's, onde n pode ser dividido em partições de 3 ou 5 elementos. Ex.: a{13}, onde 13 = 3 + 5 + 5

Resolva 1 dos exemplos acima para resolver a questão.


## [nfa-thompson]: Criação de NFA para representação de Regex na construção de Thompson

**Q1)** Utilize a construção de Thompson para criar um NFA-ε para as seguintes expressões regulares.

1. `ab|c`
2. `ab(cd|ε)`
3. `a*b*`
4. `a(b|c)d`
5. `b(a|b)*a|a`


## [nfa-epsilon]: Conversão de NFA-ε para NFA

**Q1)** O autômato abaixo representa listas de elementos formadas por sequências de a's. Responda

![Diagrama](./arquivos/nfa-epsilon-q1.svg)

1. O caminho ABEF produz a string `[]`. Encontre um caminho que aceite a string `[aa,a]`.
2. A string `[aaa` não é aceita pelo autômato. Determine o conjunto de  **todos** estados em que autômato pode estar após receber esta entrada. 

**Q2)** Remova as transições ε dos dois autômatos abaixo.

![Diagrama](./arquivos/nfa-epsilon-q2.svg)

## [nfa-dfa]: Conversão de NFA para DFA

**Q1)** Converta os autômatos abaixo para DFA.

![Diagrama](./arquivos/nfa-dfa.svg)

Resolva dois autômatos para demonstrar competência.