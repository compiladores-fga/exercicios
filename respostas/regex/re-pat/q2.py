# O programa usa expressões regulares para encontrar todas as ocorrências
# de gifs existem na página e em seguida conta quanto elas foram.

import random, re
from faker import Faker

fake = Faker("la")
output = ''


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
    output += "<!DOCTYPE html>"
    output += "<head><title>Lorem ipsum</title></head>\n"
    output += "<body>"
    # print("<!DOCTYPE html>")
    # print("<head><title>Lorem ipsum</title></head>\n")
    # print("<body>")
    h(1)

    for i in range(random.randint(10, 20)):
        output += random.choice([h, p, p, img])()
        output += "\n"
        # print(random.choice([h, p, p, img])())
        # print()
    output += "</body>"
    # print("</body>")

pattern = r".gif"

gifs = re.findall(pattern,output)
print(len(gifs))