# Re-pat

## Q1

Editor de texto: VS Code

Expressão regular utilizada: `(\d{2})/(\d{2})/(\d{4})`

Regra de substituição: `$2/$1/$3`

[Arquivo resultante](./re-pat-q1/updated-re-pat-q1.txt)

## Q2

Expressão regular: `<img src=.*\.gif`

Com a expressão regular, resta apenas utilizar alguma ferramenta para contar o número de ocorrências. Com python, por exemplo, pode-se utilizar o método findall do módulo `re` para realizar a contagem.

[Exemplo Contagem Ocorrências](./re-pat-q2/count_occurrences.py)
