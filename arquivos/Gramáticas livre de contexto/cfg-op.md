## Q1) Algumas linguagens de programação possuem operadores de composição e aplicação de funções. Por exemplo, em Elm e F#, a expressão x |> f significa executar a função f com o argumento x. Este operador é associativo à esquerda x |> f |> g = (x |> f) |> g. Já f >> g cria uma nova função que passa o argumento para f e o resultado disto para g. Este operador também é associativo à esquerda e possui uma precedência maior que |>, de forma que x |> f >> g >> h |> w pode ser interpretado como (x |> ((f >> g) >> h)) |> w.

Crie uma gramática para uma mini linguagem que inclua estes operadores e nomes como x, y, f, g, etc como símbolos terminais. Certifique-se que a gramática proposta obedece às leis de associatividade e precedência descritas acima.
'''

    gramatica   ::= funcao 

    funcao      ::= parametro '|>' (funcao | term | atribuicao)
    atribuicao  ::= term '>>' (atribuicao | term)
    parametro   ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    term        ::= 'x' | 'y' | 'f' | 'g' | 'h'
'''