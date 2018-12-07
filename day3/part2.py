claims = open("day3.input", "r").read().rstrip().split("\n")

grid = {}
overlapping = {}

for claim in claims:
    x,y = [int(e) for e in claim.split(" ")[2][:-1].split(",")]
    w, h = [int(e) for e in claim.split(" ")[3].split("x")]
    id = int(claim.split(" ")[0][1:])
    overlapping[id] = False
    for i in range(x, x+w):
        for j in range(y, y+h):
            if (i, j) not in grid:
                grid[(i, j)] = id
            else:
                overlapping[grid[(i, j)]] = True
                overlapping[id] = True
                grid[(i, j)] = -1

for id in overlapping:
    if not overlapping[id]:
        print(id)
