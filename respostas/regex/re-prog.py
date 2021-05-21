import re

test = 'aabcc'
regex = r"(a|b|c)*"
print(re.match(regex, test))

test = 'aabbaaba'
regex = r"(a|b)(a|b)*"
print(re.match(regex, test))

test = 'a'
regex = r"a|b|c|"
print(re.match(regex, test))

test = 'e'
regex = r"(a|b|c|d|e)|ab|c|"
print(re.match(regex, test))
