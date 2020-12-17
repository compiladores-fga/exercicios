### Q1
O compilador traduz o código fonte em um código executavel, código de maquina por exemplo, normalmente um arquivo binario, e então executa esse resultado. É o caso de C e C++ por exemplo.
Já o interpretador executa as instruções do código fonte diretamente, fazendo a tradução e execução delas linha a linha. É o caso de Python por exemplo.
Algumas diferenças são:
* O compilador te mostra erros no seu código logo após ser compilado, já com o interpretador os erros acontecem durante a execução
* No caso do compilador o código fonte pode ser até descartado após a compilação, pois não é utilizado na execução. O mesmo não pode ser dito para o interpretador, que utiliza o código fonte.
* O interpretador realiza as fases de análise léxica, sintática e semântica, linha a linha. Porém, a otimização já é bem mais limitada e ele não emite um código resultante, já que executa a partir do próprio código fonte. Já um compilador pode realizar todas as fases.

### Q2
[Nuitka](https://github.com/Nuitka/Nuitka) é um compilador de Python escrito em Python.