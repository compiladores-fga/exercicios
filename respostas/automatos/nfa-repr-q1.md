# 1
A diferença entre um autômato determinístico finito e um autômato não-deterministico finito é que o primeiro tem só um caminho possível para seguir de acordo com a entrada, enquanto o segundo pode conter mais de um caminho.

# 2
42 -> A - B - B -> Aceito
3.14 -> A - C - D - E - E -> Aceito
123. -> A - C - C - C - D -> Não Aceito

# 3
É possível juntar os estados B e C em um só estado, esse novo estado BC é estado final e pode receber números de 0-9 permanecendo no próprio estado ou receber um "." e avançar para o estado D.