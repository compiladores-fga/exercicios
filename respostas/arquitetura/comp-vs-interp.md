# **Q1)** Descreva as semelhanças e diferenças entre compiladores e interpretadores, em especial no que ambos diferem (ou se assemelham) com relação às etapas mencionadas na questão anterior.

Um compilador é um programa que traduz um código inteiro de uma linguagem para outra de uma vez, gerando um arquivo executável. Interpretadores não emitem o cógigo inteiro de uma vez, na verdade ele é emitido e executado na medida que o interpretador traduz o código.

Interpretadores não geram arquivos armazenados portanto executam todas as etapas de compilação todas as vezes que o programa a ser compilado precisa ser rodado.

# **Q2)** É um erro comum acreditar que "compilada" vs "interpretada" é um uma característica da linguagem de programação. Estas são características de implementações específicas da linguagem. Ainda que a implementação de Python criada por Guido seja interpretada ou que a versão do C que presente no GCC seja compilada, nada impede se crie versões compiladas de Python ou interpretadas de C. Encontre pelo menos um exemplo de implementação de um compilador para uma linguagem normalmente tida como interpretada ou de um interpretador para uma linguagem normalmente tida como compilada. Forneça uma referência como link, artigo, etc que aponte para o projeto escolhido. 

* https://www.pyinstaller.org/index.html

* https://datatofish.com/executable-pyinstaller/

Pyinstaller é um compilador de python que gera um arquivo executável a partir de cógigo python.