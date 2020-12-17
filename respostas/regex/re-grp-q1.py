import datetime
import re

text = open('re-grp-q1.txt', 'r').read()
regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})(?:T\d{2}:\d{2})?(?:\+\d{2}:\d{2})?')

dates = regex.findall(text)

birthdate = datetime.date(1997, 10, 4)
lst = []

for date in dates[1:]:
    try:
        year, month, day = date
        birthdate_diff = abs(datetime.date(int(year), int(month), int(day)) - birthdate)
        lst.append(birthdate_diff)
    except ValueError:
        continue
closest = min(lst)
closest_date = birthdate - closest 
print(f'Original(YYYY/mm/dd): {closest_date.strftime("%Y/%m/%d")}\nParsed(dd/mm/yy): {closest_date.strftime("%d/%m/%Y")}')
