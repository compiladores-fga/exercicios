## [re-pat]

### Q1

No VIM eu utilizei a regex `(\d+)/(\d+)/(\d+)` (não vi necessidade de tratar cada número) e a regra de substituição foi $2/$1/$3. 

O comando ficou:

    :%s/\(\d\+\)\/\(\d\+\)\/\(\d\+\)/\2\/\1\/\3/g 

### Q1

O próprio VIM possui uma maneira de contar o número de ocorrências de um padrão. Utilizei a expressão `img src=".+\.gif"`.

O comando ficou:

    :%s/img src=\".\+\.gif\"//gn
    
