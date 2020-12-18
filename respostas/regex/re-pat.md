**Q1)** 

```python
import random
from faker import Faker
import re
fake = Faker("la")

regex = r"([0-9][0-9][/])+"

def with_date(frase):
    date = fake.date_object()
    date = f"{date.month:02}/{date.day:02}/{date.year:04}"
    return frase.replace(random.choice(frase.split()[:-1]), date)


if __name__ == "__main__":
    for i in range(random.randint(3, 20)):
        for i in range(random.randint(4, 20)):
            frase = fake.sentence()
            if random.random() < 0.25:
                frase = with_date(frase)

            if re.search(regex, str(frase)):
                string = re.search(regex, str(frase)).group(0)
                frase = re.sub( string, string[3] + string[4] + '/' + string[0] + string[1] + '/', frase)

```
 
 * Foi-se usado a REGEX e a condição abaixo.
 
```python
regex = r"([0-9][0-9][/])+"
```

```python
            if re.search(regex, str(frase)):
                string = re.search(regex, str(frase)).group(0)
                frase = re.sub( string, string[3] + string[4] + '/' + string[0] + string[1] + '/', frase)

```


**Q2)** 

```python
import random
from faker import Faker
import re
fake = Faker("la")

regex = r"(src=\")([-\/\]|[\w0-9])*(.gif\">)"


def replace_word(st, by):
    word = random.choice(st.split())
    if not word[-1].isalnum():
        by += word[-1]
    return st.replace(word, by)


def h(n=None):
    n = n or random.randint(1, 6)
    return f'<h{n}>{fake.sentence().strip(".")}</h{n}>'


def p():
    text = fake.paragraph(nb_sentences=10)
    if random.random() < 0.33:
        text = replace_word(text, img())
    elif random.random() < 0.50:
        text = replace_word(text, img_file())

    return f"<p>{text}"


def img():
    return f'<img src="{img_file()}">'


def img_file():
    if random.random() < 0.5:
        return fake.file_path(extension="gif")
    else:
        return fake.file_path(category="image")


if __name__ == "__main__":
    print("<!DOCTYPE html>")
    print("<head><title>Lorem ipsum</title></head>\n")
    print("<body>")
    h(1)

    contgif = 0
    for i in range(random.randint(10, 20)):

        string = random.choice([h, p, p, img])()
        # print(random.choice([h, p, p, img])())
        print(string)
        print()

        if re.search(regex, string):
                stringRe = re.search(regex, str(string)).group(0)
                contgif = contgif + 1

    print("</body>")
```
* REGEX
```python
regex = r"(src=\")([-\/\]|[\w0-9])*(.gif\">)"

```
* DECLARAÇÃO DE VARIAVEL PARA CONTAR
```python
contgif = 0
```
* CONDIÇÃO PARA ENCONTRAR E CONTAR
```python
if re.search(regex, string):
        stringRe = re.search(regex, str(string)).group(0)
        contgif = contgif + 1
```
