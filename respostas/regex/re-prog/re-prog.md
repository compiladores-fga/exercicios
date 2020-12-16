# 1. r'[a-c]*'

  R:  (a|b|c)


# 2. r'[ab]+'

  R:  (a|b)(a|b)*


# 3. r'a?b?c?'

  R:  (a|)(b|)(c|)


# 4. r'[abde]|ab|c?'

  R:  (a|b|d|e)|ab|(c|)
