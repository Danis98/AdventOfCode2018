ids = open("day2.input", "r").read().split()

def diff(a, b):
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return d

found = False
for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        if diff(ids[i], ids[j]) == 1:
            found = True
            s = ""
            for k in range(len(ids[i])):
                if ids[i][k] == ids[j][k]:
                    s += ids[i][k]
            print(s)
            break
    if found:
        break
