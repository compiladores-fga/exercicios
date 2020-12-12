import random
from random import randint as rint
from faker import Faker
import re
from datetime import date

fake = Faker("la")


def replace_word(st, by):
    word = random.choice(st.split())
    if not word[-1].isalnum():
        by += word[-1]
    return st.replace(word, by)


def p():
    text = fake.paragraph(nb_sentences=10)
    for _ in range(3):
        if random.random() < 0.5:
            text = replace_word(text, dates())
    print(text)
    return text


def dates():
    date = f"{rint(1000, 2050):04}-{rint(1, 13):02}-{rint(1, 31):02}"
    if random.random() < 0.33:
        date += f"T{rint(0, 24):02}:{rint(0, 60):02}"
        if random.random() < 0.5:
            date += f"+{rint(0, 24):02}:{random.choice([0, 30]):02}"
    return date


if __name__ == "__main__":
    birthday = date(1996, 8, 26)
    dataArray = []
    aux = ''
    earliestDate = []
    for i in range(random.randint(10, 20)):
        datas = (re.findall(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", p()))
        for i in datas:
            try:
                dateCompare = date(int(i[0]), int(i[1]), int(i[2]))
                dataArray.append(dateCompare)
            except Exception as e:
                print()
                print(i)
                print(e)
                print()
            finally:
                continue
    for k in dataArray:
        earliestDate.append(abs(birthday - k))
    earliestDate.sort()
    if dataArray.count(birthday + earliestDate[0]) > 0:
        print('Data mais pŕoxima {}'.format(birthday + earliestDate[0]))
    else:
        print('Data mais pŕoxima {}'.format(birthday - earliestDate[0]))