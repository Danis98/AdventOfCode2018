res = set()
ctr = 0
prev = -1

r1 = 0
while True:
    r2 = r1 | 0x10000
    r1 = 0x65AB8E
    while True:
        r1 = (((r1 + (r2 & 0xFF)) & 0xFFFFFF) * 0x1016B) & 0xFFFFFF
        if 256>r2:
            break
        r2 = r2 >> 8
    if r1 in res:
        print(prev)
        break
    res.add(r1)
    prev = r1
    ctr += 1
