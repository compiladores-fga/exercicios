from lark import Lark, InlineTransformer, Token

grammar = Lark(
        r"""
        ?start : array
        ?array : "[" elem tail* ","? "]"
        ?tail : "," elem
        ?elem : array
              | INTEGER -> number
              | -> empty
        %import common.SIGNED_INT
        %import common.WS
        INTEGER : SIGNED_INT

        %ignore WS
        """,
        )

class JavascriptListTransformer(InlineTransformer):
    def array(self, *arg):
        return list(arg)

    def number(self, arg):
        return int(arg)

    def empty(self):
        return None

def repl():
    print("Digite comandos no prompt. O comando quit encerra a sessão.\n")
    print('O comando "debug" mostra ou oculta as árvores sintáticas intermediárias')

    tree = None
    debug = False
    transformer = JavascriptListTransformer()
    while True:
        src = input(">>> ")
        if src == "quit":
            break
        if src == "debug":
            debug = True
            if tree:
                print(tree.pretty())
            continue

        try:
            tree = grammar.parse(src)
        except Exception as e:
            print(f"Erro de sintaxe: {e}")
            continue

        if debug:
            print(tree.pretty())
        print(transformer.transform(tree))

if __name__ == "__main__":
    repl()
