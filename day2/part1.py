import string

ids = open("day2.input", "r").read().split()

two = 0
three = 0

for id in ids:
    tw = False
    th = False
    for ch in string.ascii_lowercase:
        if id.count(ch) == 2 and not tw:
            tw = True
            two += 1
        elif id.count(ch) == 3 and not th:
            th = True
            three += 1
        if tw and th:
            break

print(two*three)
