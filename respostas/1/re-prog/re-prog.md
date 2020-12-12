# re-prog

    r"[a-c]*" => r"[a|b|c]*"
    r"[ab]+"  => r"[a|b]*"
    r"a?b?c?"  => r"(a|)(b|)(c|)"
    r"[abde]|ab|c?" => r"[a|b|d|e]|ab|c"
