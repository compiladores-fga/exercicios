## [comp-org]: Compreender as etapas tradicionais de análise do código em um compilador

**Q1)** Descreva a função de cada etapa no processo de compilação de um código

1. Análise léxica
2. Análise sintática
3. Análise semântica
4. Otimização
5. Emissão de código 

### Análise léxica

<p align='justify'>A análise léxica é responsável pela leitura do código fonte de acordo com os símbolos da linguagem agrupando o código em lexemas e forma as sequências de tokens.</p>

### Análise sintática

<p align='justify'>Análise sintática ou parser é responsável pela análise da corretude dos tokens obtidos na análise léxica.</p>

### Análise Semântica

<p align='justify'>É responsável pela validação das regras da linguagem, para isso utiliza a árvore sintática e também a tabela de símbolos.</p>

### Otimização

<p align='justify'>Processo utilizado para maximizar a eficiência e diminuir gastos computacionais desnecessários, utliza heurísticas para detectar sequências de código inificiente e substituí-las.</p>

### Emissão de código

<p align='justify'>Responsável pela geração da linguagem de máquina. Processadores são incapazes de entender código de linguagens em alto nível por isso é necessário que ocorra a tradução para a arquitetura que o processador seja capaz de interpretar</p>
