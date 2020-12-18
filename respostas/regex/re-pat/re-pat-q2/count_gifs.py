import re

if __name__ == '__main__':
    with open('re-pat-q2.html', 'r') as file_:
        content = file_.read()

        reg = re.compile(r'img src=.*\.gif')
        matches = reg.findall(content)

        print("Number of gifs:", len(matches))
