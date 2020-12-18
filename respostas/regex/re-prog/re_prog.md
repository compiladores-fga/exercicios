## [re-prog]: Converter e associar expressões regulares da teoria de compiladores com expressões regulares escritas em linguagem de programação

**Q1)** Reescreva as expressões regulares Python utilizando apenas os operadores básicos de alternativa (`|`), repetição (`*`), concatenação e produções ε.

1. `r"[a-c]*"`  ->  `(a|b|c)*`
2. `r"[ab]+"`   ->  `(a|b)(a|b)*`
3. `r"a?b?c?"`  ->  `(a|ε)(b|ε)(c|ε)`
4. `r"[abde]|ab|c?"`  ->  `(a|b|d|e)|ab|(c|ε)`