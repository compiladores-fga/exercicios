import random
from random import randint as rint
from faker import Faker
import re
from datetime import datetime
fake = Faker("la")

regex = r"(([0-9][0-9])|[-])+([T]|[0-9][0-9]|[:]|[+])+"


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

if __name__ == "__main__":

    maisProximo = 366
    dias = 366

    for i in range(random.randint(10, 20)):
        texto = p()

        if re.search(regex, str(texto)):

            string = re.search(regex, str(texto)).group(0)
            string = string.split("T")

            try:

                data_e_hora = datetime.strptime(string[0], '%Y-%m-%d')
                nascimento = datetime.strptime(str(data_e_hora.year) + '-09-27', "%Y-%m-%d")
                difenca1 = abs(data_e_hora - nascimento)
                difenca2 = abs(data_e_hora - nascimento)
                difenca = min(difenca1, difenca2)
                dias = difenca.days
                
            except:
                print("Data invalida!")
                
            
            if int(maisProximo) > int(dias):
                maisProximo = dias
                dataMaisProxima = datetime.strptime(str(data_e_hora.year) + '-' + str(data_e_hora.month) + '-' + str(data_e_hora.day) , "%Y-%m-%d")

    print("Data mais proxima: ", dataMaisProxima)
    print("Menor diferença de dias: ", maisProximo)
