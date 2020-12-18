## [re-pat]: Aplicar expressões regulares para encontrar padrões de texto simples em um documento

Esta competência testa a capacidade de utilizar expressões regulares em ferramentas de do dia a dia. A maior parte dos editores possui a funcionalidade de procurar texto baseado em expressões regulares e de realizar substituições baseados nos grupos de captura. A partir de uma expressão regular do tipo `r(\d+) - (\w+)`, que captura um número e uma palavra separados por hífens, podemos criar uma regra de substituição como `$2 - $1` para inverter a ordem dos dois elementos ou qualquer outra substituição em que `$1` representa o conteúdo capturado por `(\d+)`  e `$2` por `(\w+)`.

**Q1)** O script em [arquivos/re-pat-q1.py] gera um texto que contêm várias datas no formato americano MM/DD/AAAA. Use uma regra de substituição que converta todas estas datas para o formato brasileiro DD/MM/AAAA. Diga qual expressão regular e qual regra de substituição foi utilizada no seu editor de código.  

A expressão regular utilizada: `(\d{2})/(\d{2})/(\d{4})`<br>
A regra de substituição utilizada: `$2/$1/$3`

**Q2)** O arquivo [arquivos/re-pat-q2.py] gera um html algumas tags `<img>` que fazem referências a arquivos ".gif" como em `<img src="path-to-img.gif">`. Crie uma expressão regular que encontre todas extensões `.gif` **que aparecem dentro do atributo src das tags de img**. Descreva como você poderia utilizar esta expressão em conjunto com alguma outra ferramenta para contar o número de ocorrências destas imagens no documento.

A expressão regular utilizada: `<img\src="([\d\w\/]+\.gif)">`<br>
A expresão pode ser usada para verificar todas as ocorrências da extensão `.gif` em um texto, além de poder realizar a análise do tamanho.