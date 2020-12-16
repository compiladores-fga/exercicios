## QUESTÃO: Reescreva as expressões regulares Python utilizando apenas os operadores básicos de alternativa (|), repetição (*), concatenação e produções ε.

## RESPOSTAS:

### 1. r"[a-c]*"

<code>r"(a|b|c)*"</code>

### 2. r"[ab]+"

<code>r"(a|b)(a|b)*"</code>

### 3. r"a?b?c?"

<code>(a|)(b|)(c|)</code>

### 4. r"[abde]|ab|c?"

<code>(a|b|d|e)|ab|(c|)</code>