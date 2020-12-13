## [re-prog]: Converter e associar expressões regulares da teoria de compiladores com expressões regulares escritas em linguagem de programação

#### Q1) Reescreva as expressões regulares Python utilizando apenas os operadores básicos de alternativa (|), repetição (*), concatenação e produções ε.

- r"[a-c]*"
[a|b|c]*

- r"[ab]+"
[ab][ab]*

- r"a?b?c?"
[a|ε][b|ε][c|ε]

- r"[abde]|ab|c?"
[abde]|ab|[c|ε]