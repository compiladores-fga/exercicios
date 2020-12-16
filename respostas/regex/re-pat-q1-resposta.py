import fileinput
import re

# Regex usada para capturar datas
# r'(\d{2})/(\d{2})/(\d{4})'

# Regex usada para substituição da data
# r'\2/\1/\3' ou $2/$1/$3

for line in fileinput.input(files=('datasingles.txt')):
    line = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2/\1/\3', line)

    print(line)