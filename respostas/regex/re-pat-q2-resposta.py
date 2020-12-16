import fileinput
import re

# Regex usada para capturar imagens
# r'<img src=\"([\d\w\/]+\.gif)\">'

# Pode ser utilizada com um script python, como este, que conta as ocorrencias de imagens no documento.

elementsFounded = 0

for line in fileinput.input(files=('text2.txt')):
    elementsFounded = elementsFounded + len(re.findall(r"<img src=\"([\d\w\/]+\.gif)\">", line))

print (elementsFounded)

