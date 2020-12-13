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

            dia = r"[\s|^][0-9]{2}"
            mes = r"\/[0-9]{2}\/"

            listaDia = re.findall(dia, frase)
            listaMes = re.findall(mes, frase)
            
            tempListaDia = []
            tempListaMes = []

            for i in listaDia:
                tempListaDia.append("/"+i[1:]+"/")
            for i in listaMes:
                tempListaMes.append(" "+i[1:-1])

            for i in range(0, len(listaDia)):
                frase = re.sub(listaDia[i], tempListaMes[i], frase)
                frase = re.sub(listaMes[i], tempListaDia[i], frase)

            print(frase, end=" ")

        print("\n")