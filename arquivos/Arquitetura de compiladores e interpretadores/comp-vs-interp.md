#### Descreva as semelhanças e diferenças entre compiladores e interpretadores, em especial no que ambos diferem (ou se assemelham) com relação às etapas mencionadas na questão anterior.
No geral a principal diferenca e que enquanto os compiladores executam a truducao do codigo de uma linguagem mais abstrata de alto nivel para uma linguagem mais simples de baixo nivel de uma vez so, os interpretadores vao realizando essa tarefa linha a linha, traduzindo e executando.


#### É um erro comum acreditar que "compilada" vs "interpretada" é um uma característica da linguagem de programação. Estas são características de implementações específicas da linguagem. Ainda que a implementação de Python criada por Guido seja interpretada ou que a versão do C que presente no GCC seja compilada, nada impede se crie versões compiladas de Python ou interpretadas de C. Encontre pelo menos um exemplo de implementação de um compilador para uma linguagem normalmente tida como interpretada ou de um interpretador para uma linguagem normalmente tida como compilada. Forneça uma referência como link, artigo, etc que aponte para o projeto escolhido.
Um exemplo de interpretador para uma linguagem normalmente compilada e o CINT, um interpretador de C/C++:
 - https://web.archive.org/web/20200504034257/http://root.cern.ch/cint

Um exemplo de compilador para uma linguagem normalmente interpretada e o Numba, um compilador Python:
 - https://numba.pydata.org/