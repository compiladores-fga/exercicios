## Q1) Compreender as principais diferenças entre um compilador e um interpretador.

Um compilador tem como função realizar a tradução de todas as linhas de código de uma linguagem que geralmente é de alto nível para outra linguagem normalmente de baixo nível ou mesmo código de máquina. Já o interpretador, executa linha por linha do código, sem **emitir** arquivo binário. Portanto, para cada mudança no código o mesmo precisa ser compilado novamente. O compilador costuma ser muito elaborado em questão de **otimização**, sempre buscando a melhor forma de traduzir um código, enquanto o interpretador não.

Tanto o compilador quanto o interpretador possuem **análise léxica**, **análise sintática** e **análise semântica**, se diferenciando apenas no tempo de execução e na otimização.