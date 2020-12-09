import random
from random import randint as rint
from faker import Faker

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
    date = f"{rint(1000, 2050):04}-{rint(1, 12):02}-{rint(1, 31):02}"
    if random.random() < 0.33:
        date += f"T{rint(0, 23):02}:{rint(0, 59):02}:{rint(0, 59):02}"
        if random.random() < 0.5:
            date += f"+{rint(0, 24):02}:{random.choice([0, 30]):02}"
    return date


if __name__ == "__main__":
    for i in range(random.randint(10, 20)):
        print(p())
        print()