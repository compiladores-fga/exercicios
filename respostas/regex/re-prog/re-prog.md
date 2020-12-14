1. `r"[a-c]*"`
    
    Resposta: `(a|b|c)`
2. `r"[ab]+"`

    Resposta: `(a|b)(a|b)*`
3. `r"a?b?c?"`

    Resposta: `(a|)(b|)(c|)`
4. `r"[abde]|ab|c?"`

    Resposta: `(a|b|d|e)|ab|(c|)`