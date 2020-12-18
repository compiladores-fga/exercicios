import random
import re
import datetime
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
            text = replace_word(text, data())
    return text


def data():
    date = f"{rint(1000, 2050):04}-{rint(1, 13):02}-{rint(1, 31):02}"
    if random.random() < 0.33:
        date += f"T{rint(0, 24):02}:{rint(0, 60):02}"
        if random.random() < 0.5:
            date += f"+{rint(0, 24):02}:{random.choice([0, 30]):02}"
    return date


if __name__ == "__main__":

  arrayData = []

  for i in range(random.randint(10, 20)):
    text = p()

    for i in re.findall(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", text):
      try:
        dt = datetime.date(int(i[0]), int(i[1]), int(i[2]))
        arrayData.append(dt)
      except Exception as e:
        print(e)
      finally:
        continue


  bday = datetime.date(2000, 3, 11)
  datas = []     

  for i in arrayData:
      datas.append(abs(bday - i))
  datas.sort()
  if arrayData.count(bday + datas[0]) > 0:
      print(format(bday + datas[0]))
  else:
      print(format(bday - datas[0]))