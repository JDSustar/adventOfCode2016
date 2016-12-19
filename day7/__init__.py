### I GAVE UP AND COPIED THIS ONE
### I HAD A LOT OF TROUBLE WITH THE REGEXES
### https://github.com/bpeel/advent2016/blob/master/day7.py

import re

def has_abba(s):
    return re.search(r'(.)(?!\1)(.)\2\1', s) != None

def has_tls(s):
    for md in re.finditer(r'\[.*?\]', s):
        if has_abba(md.group(0)):
            return False

    return has_abba(s)

def hypernet_has_bab(s, bab):
    for md in re.finditer(r'\[.*?\]', s):
        if md.group(0).find(bab) != -1:
            return True

    return False

def has_ssl(s):
    for outside in re.split(r'\[.*?\]', s):
        for md in re.finditer(r'(?=((.)(?!\2).\2))', outside):
            aba = md.group(1)

            if hypernet_has_bab(s, aba[1] + aba[0] + aba[1]):
                return True

    return False

with open('input.txt', 'r') as file:
    lines = file.readlines()

print("Part 1", sum(map(has_tls, lines)))
print("Part 2", sum(map(has_ssl, lines)))

