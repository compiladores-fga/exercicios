## [re-pat]: Aplicar expressões regulares para encontrar padrões de texto simples em um documento

Esta competência testa a capacidade de utilizar expressões regulares em ferramentas de do dia a dia. A maior parte dos editores possui a funcionalidade de procurar texto baseado em expressões regulares e de realizar substituições baseados nos grupos de captura. A partir de uma expressão regular do tipo `r(\d+) - (\w+)`, que captura um número e uma palavra separados por hífens, podemos criar uma regra de substituição como `$2 - $1` para inverter a ordem dos dois elementos ou qualquer outra substituição em que `$1` representa o conteúdo capturado por `(\d+)`  e `$2` por `(\w+)`.

**Q1)** O script em [arquivos/re-pat-q1.py] gera um texto que contêm várias datas no formato americano MM/DD/AAAA. Use uma regra de substituição que converta todas estas datas para o formato brasileiro DD/MM/AAAA. Diga qual expressão regular e qual regra de substituição foi utilizada no seu editor de código.  

[Código re-pat q1](https://github.com/MatheusEstanislau/exercicios/blob/master/respostas/regex/re-pat-q1.py)
<strong>Resposta: ``dataBR = (re.sub(r'([0-9]{2})/([0-9]{2})/([0-9]{4})',r'\2/\1/\3', frase))``<br>
Arquivo: resposta/regex/re-pat-q1.py
</strong>

**Q2)** O arquivo [arquivos/re-pat-q2.py] gera um html algumas tags `<img>` que fazem referências a arquivos ".gif" como em `<img src="path-to-img.gif">`. Crie uma expressão regular que encontre todas extensões `.gif` **que aparecem dentro do atributo src das tags de img**. Descreva como você poderia utilizar esta expressão em conjunto com alguma outra ferramenta para contar o número de ocorrências destas imagens no documento.

<strong>Resposta: ``<img\s+src=\"(.|..?[/a-zA-Z0-9]+\.gif)\">``</strong>

<p align="justify">Poderia realizar o método findall para encontrar todas as ocorrências e verificar se todos os gifs foram armazenados no diretório correto, caso exista algum caminho incorreto poderia ser utilizado o método re.sub para corrigir o caminho</p>