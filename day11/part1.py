serial = int(open("day11.input", "r").read().rstrip())

def get_val(x, y):
    rackID = x + 10
    power = rackID * y
    power += serial
    power *= rackID
    power = (power/100)%10
    power -= 5
    return power

def get_square(x, y):
    return sum([get_val(x+i, y+j) for i in range(3) for j in range(3)])

best = (0, 0)
bestval = 0
for x in range(298):
    for y in range(298):
        val = get_square(x, y)
        if val > bestval:
            bestval = val
            best = (x, y)
print("%d,%d -> %d" % (best[0], best[1], bestval))
