## [re-criar]: Criar padrões simples a partir dos operadores básicos de sequência, alternativas, repetição e epsilons

Resolva 2 questões para ganhar a competência.


**Q1)** Crie uma expressões regulares para cada caso abaixo:

1. Números binários múltiplos de 4, sem zeros a esquerda.

    Resposta: ```r"^[1][1|0]*00$"```

2. Datas no formato DD/MM/AAAA

    Resposta: ```r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"``` 