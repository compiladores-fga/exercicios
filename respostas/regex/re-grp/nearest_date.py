from datetime import datetime
import re

filename = 'output_re-grp-q1.txt'


def extract_dates(content):
    regex = r'(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2})?(\+\d{2}:\d{2})?'
    r = re.compile(regex)

    dates = []
    for dt in r.finditer(content):
        default_hour = 'T00:00:00'
        default_tz = '+00:00'
        dt, hour, tz = dt.groups()

        if not tz:
            tz = default_tz

        try:
            full_dt = datetime.strptime(
                f'{dt}{hour or default_hour}{(tz[:3] + tz[4:])}',
                r'%Y-%m-%dT%H:%M:%S%z'
            )

            dates.append(full_dt)
        except ValueError:
            continue

    return dates


def get_nearest_date(dates, ref_date):
    smaller_diff, result_dt = -1, None
    for dt in dates:
        diff = abs(dt-ref_date)
        if smaller_diff == -1 or diff < smaller_diff:
            smaller_diff, result_dt = diff, dt

    return result_dt


if __name__ == '__main__':
    with open(filename, 'r') as f:
        content = f.read()

    dates = extract_dates(content)
    birthday = datetime.strptime('1997-10-26T00:00:00+0000',
                                 r'%Y-%m-%dT%H:%M:%S%z')

    print('Nearest date = ', get_nearest_date(dates, birthday))
