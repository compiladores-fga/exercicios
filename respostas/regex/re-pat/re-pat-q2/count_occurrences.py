import re


if __name__ == '__main__':
    with open('re-pat-q2.txt', 'r') as f:
        content = f.read()

    reg = re.compile(r'<img src=.*\.gif')
    matches = reg.findall(content)
    print(f'number of matches = {len(matches)}')
