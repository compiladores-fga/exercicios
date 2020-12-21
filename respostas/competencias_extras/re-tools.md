* Utilizar expressões regulares para encontrar padrões e realizar substituições em editor de código.
    - Resposta: Pesquisa por cpf separado por delimitadores '.' e '-' em arquivo:
    ```re
     (\d{3})\.(\d{3})\.(\d{3})-(\d{2})
    ```
    - Para se substituir o cpf sem os delimitadores '.' e '-', basta se escrever o seguinte (feito no vscode):
    ```
    $1$2$3$4
    ```

* Utilizar expressões regulares em ferramentas de busca do Linux como grep e variantes.
    - Resposta: Procurando todos os arquivos no diretório `$HOME/Documents` com a extensão `.md` utilizando comando find com regex:
    ```sh
    find $HOME/Documents -iregex '.*\.\(md\)$'
    ```
