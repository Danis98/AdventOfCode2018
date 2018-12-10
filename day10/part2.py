point_descs = open("day10.input", "r").read().rstrip().split("\n")

p = []
v = []
for desc in point_descs:
    words = desc.replace('<', ',').replace('>', ',').split(',')
    p.append((int(words[1]), int(words[2])))
    v.append((int(words[4]), int(words[5])))

def get_bbox():
    minX = maxX = p[0][0]
    minY = maxY = p[0][1]
    for pos in p:
        minX = min(minX, pos[0])
        maxX = max(maxX, pos[0])
        minY = min(minY, pos[1])
        maxY = max(maxY, pos[1])
    return (minX, maxX, minY, maxY)

ctr = 0
while True:
    bounds = get_bbox()
    if bounds[1]-bounds[0] < 100 and bounds[3] - bounds[2] < 100:
        print("#%d - %r" % (ctr, bounds))
        grid = [['.' for i in range(bounds[0], bounds[1]+1)] for j in range(bounds[2], bounds[3]+1)]
        for pos in p:
            grid[pos[1]-bounds[2]][pos[0]-bounds[0]] = '#'
        for line in grid:
            print(''.join(line))
        input('Continue?')
    for i in range(len(p)):
        p[i] = (p[i][0]+v[i][0], p[i][1]+v[i][1])
    ctr += 1
