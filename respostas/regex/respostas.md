## re-pat

### Q1

- Resposta:

Pesquisa = (0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/(\d{4})
Regra de Substituição = $2/$1/$3

### Q2 

- Resposta:

Pesquisa = <img src=".+\.gif">
Poderia utilizar o módulo `re` do python com a regex `<img src=".+\.gif">`, se utilizar o método `re.findall` e verificar o tamanho da lista ao final do código, como mostrado no código abaixo.

```python
import re

# Arquivo re-pat-q2.txt possui o conteúdo gerado
text = open('re-pat-q2.txt', 'r').read()
regex = re.compile(r'<img src=".+\.gif">')

img_elems = regex.findall(text)

print(len(img_elems))
```


## re-grp

### Q1

```python
import datetime
import re

# Arquivo re-grp-q1.txt possui o conteúdo gerado
text = open('re-grp-q1.txt', 'r').read()
regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})(?:T\d{2}:\d{2})?(?:\+\d{2}:\d{2})?(?::\d{2}\+\d{2}:\d{2})?')

dates = regex.findall(text)

birthdate = datetime.date(1997, 10, 4)
lst = []

for date in dates[1:]:
    try:
        year, month, day = date
        birthdate_diff = abs(datetime.date(int(year), int(month), int(day)) - birthdate)
        lst.append(birthdate_diff)
    except ValueError:
        continue
closest = min(lst)
closest_date = birthdate - closest 
print(f'Original(YYYY/mm/dd): {closest_date.strftime("%Y/%m/%d")}\nParsed(dd/mm/yy): {closest_date.strftime("%d/%m/%Y")}')

```

## re-prog

### Q1

1. `r"[a-c]*"`
    * (a|b|c|ε)*
2. `r"[ab]+"`
    * (ab)(ab)*
3. `r"a?b?c?"`
    * (ε|a)(ε|b)(ε|c)
4. `r"[abde]|ab|c?"`
    * (a|b|d|e)|(ab)|(ε|c)
