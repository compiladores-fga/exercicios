### Q1
Para achar as datas podemos utilizar (\d{2})/(\d{2})/(\d{4})
Já para converte-las para o formato brasileiro usamos $2/$1/$3, que vai trocar os grupos de captura 1 e 2 de lugar, ou seja, mês e dia.

### Q2
Podemos utilizar o regex &lt;img src="(/\w+)+.gif">. Para encontrar o número de ocorrências bastaria utilizar a ferramenta Ctrl+F de qualquer editor que aceita procura por regex, como o VSCode, e o número de ocorrências será mostrado. Também seria possível criar um código em python e utilizar re.findall, que retorna todas as ocorrências, e então contar quantas foram.