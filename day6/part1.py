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

def closest(point):
    minD = 100000000000
    center_num = -1
    for i in range(len(centers)):
        center = centers[i]
        d = abs(center[0] - point[0]) + abs(center[1] - point[1])
        if minD > d:
            minD = d
            center_num = i
        elif minD == d:
            center_num = -1
    return center_num

def bfs(center_id):
    q = queue.Queue()
    q.put(centers[center_id])
    visited = set()
    area = 0
    while not q.empty():
        if area > 50000:
            return 0
        point = q.get()
        if closest(point) != center_id or (point[0], point[1]) in visited:
            continue
        visited.add((point[0], point[1]))
        area += 1
        if (point[0]-1, point[1]) not in visited:
            q.put([point[0]-1, point[1]])
        if (point[0]+1, point[1]) not in visited:
            q.put([point[0]+1, point[1]])
        if (point[0], point[1]-1) not in visited:
            q.put([point[0], point[1]-1])
        if (point[0], point[1]+1) not in visited:
            q.put([point[0], point[1]+1])
    return area

max_area = 0
for i in range(len(centers)):
    center = centers[i]
    if center[0] == minX or center[0] == maxX or center[1] == minY or center[1] == maxY:
        continue
    area = bfs(i)
    max_area = max(max_area, area)
print(max_area)
