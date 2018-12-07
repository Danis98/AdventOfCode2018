import queue

centers = [[int(c) for c in line.split(",")] for line in open("day6.input", "r").read().rstrip().split("\n")]

minX = centers[0][0]
maxX = centers[0][0]
minY = centers[0][1]
maxY = centers[0][1]

for center in centers:
    minX = min(minX, center[0])
    maxX = max(maxX, center[0])
    minY = min(minY, center[1])
    maxY = max(maxY, center[1])

def sum_dist(point):
    d = 0
    for center in centers:
        d += abs(center[0] - point[0]) + abs(center[1] - point[1])
    return d

area = 0
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        if sum_dist((x, y)) < 10000:
            area += 1

print(area)
