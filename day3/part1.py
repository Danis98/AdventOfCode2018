claims = open("day3.input", "r").read().rstrip().split("\n")

grid = {}
overlap = 0

for claim in claims:
    x,y = [int(e) for e in claim.split(" ")[2][:-1].split(",")]
    w, h = [int(e) for e in claim.split(" ")[3].split("x")]
    for i in range(x, x+w):
        for j in range(y, y+h):
            if (i, j) in grid and grid[(i, j)] == 1:
                overlap += 1
                grid[(i, j)] = 2
            elif (i, j) not in grid:
                grid[(i, j)] = 1
print(overlap)
