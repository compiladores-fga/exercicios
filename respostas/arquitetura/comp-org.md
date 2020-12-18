## [comp-org]: Compreender as etapas tradicionais de análise do código em um compilador

**Q1)**


1. Análise léxica


* É o processo de analisar entradas de linhas de caracteres, analisar se os mesmo estão adequados e produzir uma sequência de símbolos chamado "símbolos léxicos", ou somente "símbolos"(tokens), estes podem ser manipulados mais facilmente por um parser.


2. Análise sintática

* A análise sintática (parsing) é o processo onde o compilador, é a segunda fase da compilação onde se analisa uma sequência que foi dada entrada para verificar sua estrutura gramatical segundo uma determinada gramática formal. Aprova ou não as entradas. 


3. Análise semântica

* A análise semântica é o processo onde o compilador verifica os erros semânticos nas entradas e são coletadas as informações necessárias para a próxima fase da compilação.

4. Otimização

* É a ultima etapa na geração de código pelo compilador. Apos os processos anteriores diversas situações contendo sequências de código ineficiente podem ocorrer. O objeto da etapa de otimização de código é aplicar um conjunto de heurísticas para detectar tais seqüências e substituí-las por outras que removam as situações de ineficiência.

5. Emissão de código 

* A tradução do código de alto nível para o código do processador está associada à traduzir para a linguagem-alvo a representação da árvore gramatical obtida para as diversas expressões do programa. Embora tal atividade possa ser realizada para a árvore completa após a conclusão da análise sintática, em geral ela é efetivada através das ações semânticas associadas à aplicação das regras de reconhecimento do analisador sintático.
