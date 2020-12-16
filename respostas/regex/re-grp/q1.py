import re
import datetime

f = open("q1_entrada", "r")
text = f.read()

regex = r"(?:(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}))(?:T(?P<hour>\d{2}):(?P<minute>\d{2}))?(?:\+(?P<gmt_hour>\d{2}):(?P<gmt_minute>\d{2}))?"

regex = re.compile(regex)

target = datetime.date(1997, 3, 22)
nearest_date = target
smallest_delta = None

for found in regex.finditer(text):
    groups = found.groupdict()
    print(groups)
    try:
        found_date = datetime.date(int(groups["year"]), int(groups["month"]), int(groups["day"]))
        print(found_date)
        delta = abs(found_date - target)
        print(f"Delta of {found_date} is {delta}")
        if smallest_delta == None:
            smallest_delta = delta
        else:
            if (delta < smallest_delta):
                smallest_delta = delta
                nearest_date = found_date
    except ValueError as e:
        print(f"Invalid date {groups}");
    print()

print(f"Closest date to target {target} is {nearest_date} with delta of {smallest_delta}")
f.close()
