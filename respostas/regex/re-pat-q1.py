import random
from faker import Faker
import re

fake = Faker("la")


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
                dataBR = (re.sub(r'([0-9]{2})/([0-9]{2})/([0-9]{4})',r'\2/\1/\3', frase))
                print(dataBR, end=" ")

        print("\n")
