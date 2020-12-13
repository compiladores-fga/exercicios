import random
from random import randint as rint
from faker import Faker
import re
from datetime import date, datetime

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
            text = replace_word(text, date())
    return text


def date():
    date = f"{rint(1000, 2050):04}-{rint(1, 13):02}-{rint(1, 31):02}"
    if random.random() < 0.33:
        date += f"T{rint(0, 24):02}:{rint(0, 60):02}"
        if random.random() < 0.5:
            date += f"+{rint(0, 24):02}:{random.choice([0, 30]):02}"
    return date

vetor = []

if __name__ == "__main__":
    for i in range(random.randint(10, 20)):
        texto = p()
        # print(texto)
        # print()

        for j in re.findall(r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2})?(\+[0-9]{2}:[0-9]{2})?", texto):
            data = str(j[0])
            mes = int(data[5:7])
            dia = int(data[8:])

            if mes<13 and dia<32:
                try:
                    data = datetime.strptime(data, '%Y-%m-%d')
                    vetor.append(data)
                except:
                    continue

    aniversario = datetime.strptime('1995-04-30', '%Y-%m-%d')
    menor = abs((vetor[0] - aniversario).days)
    data = vetor[0]
    for i in vetor:
        temp = abs((i - aniversario).days)
        if temp<menor:
            data = i

    print(data)