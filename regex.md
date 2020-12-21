Expressões regulares e análise léxica
=====================================

**ATENÇÂO:** Alguns exercícios deste módulo utilizam o módulo Faker para gerar valores aleatórios. Instale-o utilizando o comando `pip install Faker`. 


## [re-ler]: Compreender e elicitar a linguagem gerada por expressões regulares simples

Resolva 2 questões para ganhar a competência.

**Q1)** Associe a linguagem regular às strings incluídas em cada linguagem. A relação é de muitos para muitos.

------------------------------------------------------
Regex          | String
======================================================
`0|1(1|0)*0`   | `010`
`(1|0)+`       | `101`
`1(11)*`       | `111`
`1|(11)*`      | ` `
`0*|1*`        | `00`


**Q2)** Resolva um problema da categoria "intermediate" ou "experienced" do site Regex Crosswords (https://regexcrossword.com/challenges/intermediate/puzzles/5). Anexe um screenshot ou digite a resposta aqui como prova da solução.

![printRegexcrossword](./assets/regexcrossword.png)

**Q3)** Discuta se é possível criar um conjunto de exemplos de strings para cada linguagem em Q1 de tal forma que cada exemplo seja aceito por apenas uma linguagem? Em caso positivo, dê um exemplo e em caso negativo, explique o motivo. 



## [re-criar]: Criar padrões simples a partir dos operadores básicos de sequência, alternativas, repetição e epsilons

Resolva 2 questões para ganhar a competência.


**Q1)** Crie uma expressões regulares para cada caso abaixo:

1. Números binários múltiplos de 4, sem zeros a esquerda.

    Resposta: ```r"^[1][1|0]*00$"```

2. Datas no formato DD/MM/AAAA

    Resposta: ```r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"```   

3. Endereços de e-mail com <nome>@<dominio>.<com>.<br>. O domínio pode conter qualquer número de sub-domínios e cada parte, incluindo o nome é formada por letras ou hífens.
    
    Resposta: ```r"^[^@]+@[^@]+\.[^@]{1,}$"```

**Q2)** O dicionário abaixo contêm uma associação de expressões regulares e valores. Você deve inventar valores para cada entrada de tal modo que cada par (regex, st) possua as seguinte propriedades:

1. A string st é um exemplo válido da linguagem definida pela regex no par.
2. A string **não** é reconhecida por nenhuma outra expressão regular no dicionário.

```
{
    r"abc"          : "...",
    r"(ab|c)*"      : "...",
    r"(ab|cd)+"     : "...",
    r"a{2,4}b{2,4}" : "...",
    r"ab(bc)?"      : "...",
    r"(a|b|c)*"     : "...",
}
```

Caso não seja possível incluir todas expressões regulares, elimine o menor número possível de entradas para satisfazer as propriedades acima. Um exemplo de solução com somente duas expressões regulares seria `{r"abc": "abc", r"ab(bc)?": "abbc"}`. Existem soluções com mais alternativas. 

**Q3)** Mude as regras do exercício anterior para que em cada par (regex, st)

1. A string st **não** é um exemplo válido da linguagem definida pela regex no par.
2. A string é reconhecida **todas** as outras expressões regulares no dicionário.

Encontre o maior dicionário possível com esta propriedade.


**Q4)** Criar um puzzle de pelo menos 6 letras na sessão "Player Puzzles" do site Regex Crosswords (ex.: https://regexcrossword.com/playerpuzzles/5fc9b3b284397).



## [re-prog]: Converter e associar expressões regulares da teoria de compiladores com expressões regulares escritas em linguagem de programação

**Q1)** Reescreva as expressões regulares Python utilizando apenas os operadores básicos de alternativa (`|`), repetição (`*`), concatenação e produções ε.

1. `r"[a-c]*"`
   Resposta: `r"(a|b|c)*`
2. `r"[ab]+"`
   Resposta: `r"(a|b)(a|b)*`
3. `r"a?b?c?"`
   Resposta: `r"(a|)(b|)(c|)`
4. `r"[abde]|ab|c?"`
    Resposta: `r"(a|b|d|e)|ab|(c|)`



## [re-pat]: Aplicar expressões regulares para encontrar padrões de texto simples em um documento

Esta competência testa a capacidade de utilizar expressões regulares em ferramentas de do dia a dia. A maior parte dos editores possui a funcionalidade de procurar texto baseado em expressões regulares e de realizar substituições baseados nos grupos de captura. A partir de uma expressão regular do tipo `r(\d+) - (\w+)`, que captura um número e uma palavra separados por hífens, podemos criar uma regra de substituição como `$2 - $1` para inverter a ordem dos dois elementos ou qualquer outra substituição em que `$1` representa o conteúdo capturado por `(\d+)`  e `$2` por `(\w+)`.

**Q1)** O script em [arquivos/re-pat-q1.py] gera um texto que contêm várias datas no formato americano MM/DD/AAAA. Use uma regra de substituição que converta todas estas datas para o formato brasileiro DD/MM/AAAA. Diga qual expressão regular e qual regra de substituição foi utilizada no seu editor de código.  

<strong>Resposta: ``dataBR = (re.sub(r'([0-9]{2})/([0-9]{2})/([0-9]{4})',r'\2/\1/\3', frase))``<br>
Arquivo: resposta/regex/re-pat-q1.py
</strong>

**Q2)** O arquivo [arquivos/re-pat-q2.py] gera um html algumas tags `<img>` que fazem referências a arquivos ".gif" como em `<img src="path-to-img.gif">`. Crie uma expressão regular que encontre todas extensões `.gif` **que aparecem dentro do atributo src das tags de img**. Descreva como você poderia utilizar esta expressão em conjunto com alguma outra ferramenta para contar o número de ocorrências destas imagens no documento.

Resposta: ``<img\s+src=\"(.|..?[/a-zA-Z0-9]+\.gif)\">``

<p align="justify">Poderia realizar o método findall para encontrar todas as ocorrências e verificar se todos os gifs foram armazenados no diretório correto, caso exista algum caminho incorreto poderia ser utilizado o método re.sub para corrigir o caminho</p>

## [re-grp]: Aplicar expressões regulares e utilizar grupos e sub-padrões para extrair informação a partir de um texto

**Q1)** Crie um programa para identificar datas no formato `AAAA-MM-DDTHH:MM:SS+HH:MM`, onde tanto a parte da hora (`THH:MM:SS`) quanto a parte do fuso horário (`+HH:MM`) são opcionais. Extraia a informação como um objeto do tipo `datetime.date()` para validar o mês e dia e determine qual data encontrada no texto é a mais próxima do seu aniversário.

O texto de exemplo pode ser gerado pelo arquivo [arquivos/re-grp-q1.py].

<strong>Resposta está no aquivo: re-grp-q1.py localizado no diretorio: respostas/regex</strong>


## [lex-ler]: Compreender a motivação e mecanismos da análise léxica

**Q1)** Identifique os lexemas do código abaixo.

```python
def fat(n):
    """Calcula o fatorial de um número"""
    return n * fat(n - 1) if n else 1
```

Quantos lexemas foram encontrados?

**Q2)** Temos abaixo 3 exemplos de código Python que resolvem o mesmo problema de imprimir os fatoriais de 1 até o valor fornecido pelo usuário. Cada um foi vencedor de um concurso de "code golf" em uma categoria diferente. Você consegue apontar qual o critério de "menor" programa foi utilizado em cada caso?

```python
# Solução 1
print('\n'.join(map(str, map((lambda f: lambda n: f(n, f))(lambda n, f: n * f(n - 1, f) if n else 1), range(1, int(input()) + 1)))))

# Solução 2
resultado = 1
for n in range(int(input())):
    resultado *= n + 1
    print(fat)

# Solução 3
r=1
[print(r:=r*(i+1)) for i in range(int(input()))]
```  


## [lex-re]: Criar um analisador léxico baseado em expressões regulares utilizando alguma biblioteca de apoio

**Q1)** A maior parte das linguagens de programação possui uma estrutura léxica relativamente parecida entre si. Podemos criar um analisador léxico genérico que funciona de forma aproximadamente correta em boa parte das linguagens utilizando as sequintes regras: 

* Nomes são formados por letras, números (exceto na primeira posição) e underscores.
* Números possuem dígitos e parte decimal opcional.
* Delimitadores são formados por `{}[]()`.
* Strings são formadas por qualquer caracter, exceto quebra de linha entre aspas simples ou duplas.
* Operadores são sequências com os símbolos `+-*/?<>=|&~!@%^:,;`.
* Espaços em branco são ignorados.
   
Crie um programa que realize a análise léxica a partir desta linguagem genérica e conte o número de tokens em uma string de código. Você pode utilizar o Lark ou implementar o analisador léxico utilizando somente as bibliotecas padrão da linguagem.
