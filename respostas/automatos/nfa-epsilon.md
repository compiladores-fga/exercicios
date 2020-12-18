## [nfa-epsilon]: Conversão de NFA-ε para NFA

**Q1)** 

1. 

```
Caminho ABCDCDCDEF produz a string '[aa,a]
```
2.  

```
1 - Um dos caminhos é ABE, fica travado em E;
2 - Outro caminho é ABCD(E)CD(E)CD(E)C

Ele possa em algum momento pelos estados ABCDE, o unico que não passa é o estado F.

Todos os estados que ele pode estar ao fim é C,D ou E.
```


**Q2)** 

<img src="/imagens/imagens_automatos/nfa-epsilon-2-a.png" width="800">


<img src="/imagens/imagens_automatos/nfa-epsilon-2-B.png" width="800">
