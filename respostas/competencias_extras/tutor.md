# Configurando integração contínua com github actions

Para se configurar uma integração contínua utilizando o github-actions basta se seguir os seguintes passos:

- Criar o dirétorio `.github/workflows` desde a raíz do seu projeto no github e adicionar um arquivo com o nome `python-app.yml` 
- Após isso deve ser realizada a configuração de como o pipeline deve ser executado, para a disciplina de compiladores foi utilizado somente o `pytest` para realização dos testes e o `flake8` como um linter.

## Configuração do arquivo `python-app.yml`:

- Inicialmente deve se escolher o nome do pipeline e também quando o pipeline deve ser executado. O exemplo a seguir define a execução do pipeline em todo `push` de um commit para o github:

```yml
name: Python application

on: [push]
```

- Após isso são definidos os jobs a serem executados, os jobs definidos nesse exemplo são bem simples e definem que o pipeline será executado em um sistema operacional `ubuntu` com o python na versão `3.8`:

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    
```

- Com o sistema operacional e a versão do python definidos basta se executar os testes, porém é necessário realizar a instalação das dependências de todos os programas contidas em um arquivo `requirements.txt`. Após isso o teste é executado utilizando o pytest e uma variável de ambiente `TEST_FILE`, com o nome do arquivo dos testes a serem executados:

```yml
- name: Install dependencies
    run: pip install -r requirements.txt
- name:  Run tests
    run: pytest $TEST_FILE
    env:
    TEST_FILE: test_parser.py
```

- O arquivo `python-app.yml` fica assim após toda a configuração:

```yml
name: Python application

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name:  Run tests
      run: pytest $TEST_FILE
      env:
        TEST_FILE: test_parser.py
``` 


Para maiores detalhes, acesse a [documentação do github Actions](https://docs.github.com/en/free-pro-team@latest/actions/guides/building-and-testing-python)