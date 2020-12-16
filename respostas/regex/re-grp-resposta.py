import fileinput
import re
from datetime import datetime, timezone

# Regex usada para capturar datas
# r'(\d{2})/(\d{2})/(\d{4})'

# Regex usada para substituição da data
# r'\2/\1/\3' ou $2/$1/$3


aniversario = datetime.strptime("20/01/1998", "%d/%m/%Y")
lista = []
novalista = []
dif = []

for line in fileinput.input(files=('q1.txt')):
    line = re.sub(r'(\d{4})-(\d{2})-(\d{2})(T(\d{2}:\d{2})(:\d{2})*(\+(\d{2}:\d{2}))*)*', r'\3/\2/\1' , line)

    lista =  re.findall(r'(\d{2}/\d{2}/\d{4})', line)
    try:
        for date in lista:
            novalista.append(datetime.strptime(date, "%d/%m/%Y"))
            dif.append(abs(aniversario - datetime.strptime(date, "%d/%m/%Y")))
    except ValueError:
        pass
        #Ignora essas datas

print( novalista[dif.index(min(dif))] )