1. Análise Léxica: Etapa responsável por ler caractere por caractere do código fonte, agrupa os caracteres em lexemas e produz uma sequência de símbolos chamados Tokens.

2. Análise Sintática: Também chamado de parser, essa etapa valida os tokens obtidos na etapa anterior para identificar se a lista de tokens possui sentenças válidas para aquela linguagem de programação, gerando uma árvore sintática do programa.

3. Análise Semântica: A análise semântica é responsável por verificar aspectos relacionados ao significado das instruções. Nesse momento ocorre a validação de uma série de regras não verificadas nas etapas anteriores.
A análise semântica percorre a árvore sintática gerada , relaciona os identificadores com seus dependentes de acordo com a hierárquia. Essa etapa também captura informações sobre o programa fonte para que as fases subsequentes gerem o código objeto. Além disso, nessa etapa também ocorre a verificação de tipos, onde o compilador verifica se cada operador recebe os operandos permitidos e especificados na linguagem fonte.

4. Otimização: O objetivo desta etapa é aplicar um conjunto de heurísticas para detectar quais sequências de código ineficiente, e substítui-las por outras que removam as situações de ineficiência. Estas técnicas de otimização devem manter o significado do programa original, além de serem capazes de capturar a maior parte das possibilidades de melhoria de código dentro de limites razoáveis de esforço gasto.

5. Emissão de Código: A fase final consiste na geração de código para o programa objeto, consistindo normalmente no código em linguagem assembly ou em linguagem de máquina. Aqui é o processo de converter as instruções identificadas para instruções em linguagem de máquina.