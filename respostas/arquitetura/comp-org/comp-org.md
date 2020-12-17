# Q1 comp-org
## 1 Análise léxica
A **análise léxica** também conhecida como scanner ou leitura é a primeira fase de um processo de compilação e sua função é fazer a leitura do programa fonte, caractere a caractere, agrupar os caracteres em lexemas e produzir uma sequência de símbolos léxicos conhecidos como tokens.<br>
O analisador léxico deve interagir com a tabela de símbolos inserindo informações de alguns tokens, como por exemplo os identificadores. A nível de implementação a analise léxica normalmente é uma sub-rotina da análise sintática formando um único passo, porem ocorre uma divisão conceitual para simplificar a modularizarão do projeto de um compilador.

## 2 Análise sintática
O analisador sintático também conhecido como *parser* tem como tarefa principal determinar se o programa de entrada representado pelo fluxo de tokens possui as sentenças válidas para a linguagem de programação.<br>
A analise sintática é a segunda etapa do processo de compilação e na maioria dos casos utiliza **gramáticas livres de contexto** para especificar a sintaxe de uma linguagem de programação.

## 3 Análise semântica
A **analise semântica** é responsavel por verificar aspectos relacionados ao significado das instruções, essa é a terceira etapa do processo de compilação e nesse momento ocorre a validação de uma serie regras que não podem ser verificadas nas etapas anteriores.<br>
Muitas verificações devem ser realizadas com meta-informações e com elementos que estão presentes em vários pontos do código fonte, distantes uns dos outros. O analisador semântico utiliza a árvore sintática e a tabela de símbolos para fazer as analise semantica.

## 4 Otimização
A etapa de **otimização** é realizada pelo compilador para refinar o código, de forma que vícios como duplicidade, redundância e não ocorrência sejam removidos no momento da compilação, para, assim, deixar o código original mais enxuto, com o mesmo resultado, reduzindo o uso de memória e processamento.

## 5 Emissão de código
A **emissão de código** é a etapa responsável por "traduzir" o código de mais alto nível, como C/C++, Swift, etc, em linguagem de máquina para ser devidamente interpretada pelo processador. 