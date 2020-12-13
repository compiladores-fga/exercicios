## Descreva a função de cada etapa no processo de compilação de um código

#### Análise léxica
E utilizada para converter uma sequencia de caracteres em uma sequencia de tokens, tokens esses que nada mais sao que um conjunto de strings com um significado, por exemplo os tokens gerados apos a execucao do parse pelo Lark.

#### Análise sintática
Fase em que e utilizado os tokens gerados pela analise lexica para construir uma estrutura de dados, que no geral e uma arvore sintatica para realizacao de um processamento posterior.

#### Análise semântica
A analise semantica utiliza a estrutura gerada pela analise sintatica e a transforma em uma representacao mais adaptada e simples para gerar codigo. Alem disso a analise semantica tambem e responsavel por analisar a utilizacao de identificadores e ligar cada um deles a declaracao.

#### Otimização
Utilizado para fazer uma otimizacao do codigo gerado pelas etapas anteriores, buscando um codigo que execute com maior eficiencia.

#### Emissão de código
Geracao do codigo final produzido pelo compilador.