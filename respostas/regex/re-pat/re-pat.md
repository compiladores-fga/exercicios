# Q1.

Utilizei a regex `(\d{2})/(\d{2})/(\d{4})` no VSCode para buscar as datas e a regra de substituição `$2/$1/$3`,
convertendo as datas para o formato brasileiro.

# Q2.

Utilizando o pacote `re`, primeiro criei armazenei o texto que é gerado a partir do arquivo [arquivos/re-pat-q2.py]
em `text`, a regex `r'<img\ssrc="([\d\w\/]+\.gif)">'` em `gif_regex` que é utilizada para encontrar os arquivos `.gif`.
Utilizando `re.findall(gif_regex, text)` encontro todos os arquivos `.gif` e calculo a quantidade dos mesmos com a
função `len()`, a solução se encontra no arquivo [respostas/regex/re-pat/re-pat.py].