### Q1
No VSCode usei a regex (\d{2})/(\d{2})/(\d{4}) para encontrar as datas e a regra $2/$1/$3 para convertê-las para o fromato brasileiro.

### Q2
Novamente no VSCode, importei o módulo "re" e criei três variáveis: uma com o texto (gerado a partir do arquivo [arquivos/re-pat-q2.py]), uma com a regex e outra com as respostas. Usei a regex <img src=\"(/\w+)+.gif\"> para encontrar os arquivos ".gif". Então igualei a variável das respostas à re.findall(r"<img src=\"(/\w+)+.gif\">", <variável do texto>) para encontrar todos os arquivos ".gif". Por fim, usei a função len() para calcular o tamanho da variável das repostas.
