import re

triangles = []

with open('input.txt', 'r') as file:
    possible = 0
    triangle1 = []
    triangle2 = []
    triangle3 = []

    for line in file:
        columns = re.split('\s+', line.strip())
        columns = [int(x) for x in columns]
        triangle1.append(columns[0])
        triangle2.append(columns[1])
        triangle3.append(columns[2])
        if len(triangle1) == 3:
            triangles.append(triangle1)
            triangles.append(triangle2)
            triangles.append(triangle3)
            triangle1 = []
            triangle2 = []
            triangle3 = []

for t in triangles:
    t.sort()
    if t[0] + t[1] > t[2]:
        possible += 1


print possible
