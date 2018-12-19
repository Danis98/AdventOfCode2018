import time
import sys

sys.setrecursionlimit(5000)

lines = open("day17.input", "r").read().rstrip().split("\n")

def print_grid():
    for line in grid:
        l = ""
        for e in line:
            if e == '.':
                l += e
            elif e == '#':
                l += '\x1b[0;37;41m' + e + '\x1b[0m'
            elif e == '+':
                l += '\x1b[0;37;46m' + e + '\x1b[0m'
            elif e == '~':
                l += '\x1b[0;37;44m' + e + '\x1b[0m'
        print(l)

veins = []
for line in lines:
    v = {}
    for half in line.split(", "):
        coord, rng = half.split("=")
        if '..' in rng:
            c1, c2 = [int(e) for e in rng.split("..")]
            v[coord] = range(c1, c2+1)
        else:
            v[coord] = [int(rng)]
    veins.append(v)

bounds = [500, 500, 0, 0]

for vein in veins:
    bounds[0] = min(bounds[0], min(vein['x']))
    bounds[1] = max(bounds[1], max(vein['x']))
    bounds[2] = min(bounds[2], min(vein['y']))
    bounds[3] = max(bounds[3], max(vein['y']))

bounds[0] -= 1
bounds[1] += 1

grid = [['.' for i in range(bounds[0], bounds[1]+1)] for j in range(bounds[2], bounds[3]+1)]

for vein in veins:
    for y in vein['y']:
        for x in vein['x']:
            grid[y-bounds[2]][x-bounds[0]] = '#'

grid[0-bounds[2]][500-bounds[0]] = '+'

def flow_water(pos, spreading):
    try:
        x, y = pos
        gx, gy = x-bounds[0], y-bounds[2]
        grid[gy][gx] = '+'
        if y == bounds[3]:
            return True
        if grid[gy+1][gx] == '+':
            return True
        if grid[gy+1][gx] == '.':
            if flow_water((x, y+1), False):
                return True
        if grid[gy][gx-1] == '.':
            l = flow_water((x-1, y), True)
        else:
            l = False
        if grid[gy][gx+1] == '.':
            r = flow_water((x+1, y), True)
        else:
            r = False
        flowing = l or r
        if not flowing and not spreading:
            xx = gx
            while xx >= 0 and grid[gy][xx] == '+':
                grid[gy][xx] = '~'
                xx -= 1
            xx = gx+1
            while xx < len(grid[gy]) and grid[gy][xx] == '+':
                grid[gy][xx] = '~'
                xx += 1
        return flowing
    except Exception as e:
        print(e)
        print_grid()
        exit(0)

flow_water((500, 0), False)

print_grid()

ctr = 0
count = False
for line in grid:
    for e in line:
        if e == '#':
            count = True
        if e in '~' and count:
            ctr += 1

print(ctr)
