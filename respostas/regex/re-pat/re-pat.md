## Q1

Expressão Regular: ```(\d{2})/(\d{2})/(\d{4})```

Regra de Substituição: ```$2/$1/$3```

## Q2

Expressão Regular: ```<img\ssrc="([\d\w\/]+\.gif)">```

Possível utilidade: Poderia ser utilizado um script que iteraria por todas as ocorrências da expressão regular salvando o conteúdo do atributo src das tags de imagem, é possível coletar esses endereços utilizando a expressão ```$1```, e utilizar esses endereços para acessar o arquivo do gif e salva-lo.