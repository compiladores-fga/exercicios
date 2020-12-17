import re
from datetime import date as package_date

pattern = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2})(?P<time>T\d{2}:\d{2}\d{0,2})?(?P<timezone>\+\d{2}\:\d{2})?')

data = None 

with open('./re-grp-q1-out', 'r') as txt:
    data = txt.read()


target_date = package_date(year=2020, month=4, day=28)

date_pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')

result = []

for date, _, _ in pattern.findall(data):

    match = date_pattern.match(date)

    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))

    try:
        temp = package_date(year=2020, month=month, day=day)

        c = abs(target_date.toordinal() - temp.toordinal())
        result.append((c, temp))
    except Exception as error:
        print(f'Error: {(day, month)}')
        print(error)
        # we have some wrong date ex: 1487-13-07
        continue


min_element = min(result, key=lambda x:x[0])
print(f'Min: {min_element}')
print(f'Result: {min_element[1]}')
