## Q1

**Editor**: Vim 8.2  
**Regex**: (\d{2})/(\d{2})/(\d{4})   
**Regra de substituição:** /\2/\1/\3  
**Comando no Vim**: %s@\(\d\{2}\)/\(\d\{2}\)/\(\d\{4}\)@\2/\1/\3@g  
**Resultado**: [result-re-pat-q1.txt](./re-pat-q1/result-re-pat-q1.txt)

## Q2
**Regex**: `r"img src=.*\.gif"`  
**Quantidades .gif**: 4  
**Solução**: [count_gifs](./re-pat-q2/count_gifs.py)  
Basta usar o `findall` da biblioteca `re` com a regex acima para contar a quantidade de ocorrências de .gif
