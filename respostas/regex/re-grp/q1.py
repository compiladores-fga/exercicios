from datetime import datetime
import os, re

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

os.system('python ../../../arquivos/re-grp-q1.py >> text')

put = open('text').read()

pattern = r"([0-9][0-9][0-9][0-9]-(0[0-9]|1[0-2])-(0[0-9]|[1-2][0-9]|30))(T([0-1][0-9]|[2][0-3]):([0-5][0-9]))?(\+([0-1][0-9]|2[0-3]):[0-9][0-9])?"

dates = re.findall(pattern,put)
concat_dates = []
for date in dates:
    date = (date[0], date[3], date[6])
    try:
        concat_dates.append(datetime.fromisoformat(''.join(date)).timestamp())
    except:
        1+1


print(datetime.fromtimestamp(nearest(concat_dates, datetime.fromisoformat('2000-03-17').timestamp())))

