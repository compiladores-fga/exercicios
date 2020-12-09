## Q1

Expressão Regular: `(\d{2})/(\d{2})/(\d{4})`
Regra de Substituição: `$2/$1/$3`

## Q2

Expressão Regular: `<img\ssrc="([\d\w\/]+\.gif)">`
Possível utilidade: Interaria por todas as ocorrências da expressão para salvar o no src da imagem. Ultilizandoa expressão `$1`, coletaria os endereços e utilizaria para acessar o arquivo do gif para salva-lo.
