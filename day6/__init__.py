from collections import defaultdict
from collections import OrderedDict

message = [
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
]

with open('input.txt', 'r') as file:
    for l in file:
        for index, c in enumerate(l):
            if index > 7:
                continue
            message[index][c] += 1

for d in message:
    dOrdered = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print dOrdered
