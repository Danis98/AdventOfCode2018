serial = int(open("day11.input", "r").read().rstrip())

def get_val(x, y):
    rackID = x + 10
    power = rackID * y
    power += serial
    power *= rackID
    power = (power/100)%10
    power -= 5
    return power

grid = [[get_val(x+1, y+1) for y in range(300)] for x in range(300)]
rowcum = [[grid[x][y] for y in range(300)] for x in range(300)]
for x in range(1, 300):
    for y in range(300):
        rowcum[x][y] += rowcum[x-1][y]

def get_square(x, y, size):
    s = 0
    for i in range(x, x+size):
        s += sum(grid[i][y:y+size])
    return s

def get_sum(x1, x2, y):
    return rowcum[x2][y] - (rowcum[x1-1][y] if x1 > 0 else 0)


best = (0, 0)
bestval = 0
sz = 0
for size in range(1, 301):
    for x in range(0, 300-size):
        window = get_square(x, 0, size)
        for y in range(0, 300-size):
            if window > bestval:
                sz = size
                bestval = window
                best = (x+1, y+1)
            if y != 300-size:
                window += get_sum(x, x+size-1, y+size) - get_sum(x, x+size-1, y)
print("%d,%d,%d -> %d" % (best[0], best[1], sz, bestval))
