import datetime
import re

text = open('re-pat-q2.txt', 'r').read()
regex = re.compile(r'<img src=".+\.gif">')

img_elems = regex.findall(text)

print(f'Ocorrencias: {len(img_elems)}')
