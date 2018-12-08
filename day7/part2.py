instructions = open("day7.input", "r").read().rstrip().split("\n")

graph = {}
deps = {}
satisfied = {}
available = []

for instruction in instructions:
    words = instruction.split(" ")
    a = words[1]
    b = words[7]
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    if a not in deps:
        deps[a] = []
    if b not in deps:
        deps[b] = []
    satisfied[a] = False
    satisfied[b] = False
    graph[a].append(b)
    deps[b].append(a)

for ch in deps:
    if deps[ch] == []:
        available.append((0, ch))

available = sorted(available)

workers = [0 for i in range(5)]
while len(available) > 0:
    cur = available[0]
    satisfied[cur[1]] = True
    available.remove(cur)

    worker = workers.index(min(workers))
    workers[worker] = max(workers[worker], cur[0]) + 60 + (ord(cur[1])-ord("A")+1)

    for ch in graph[cur[1]]:
        av = True
        for dep in deps[ch]:
            if not satisfied[dep]:
                av = False
                break
        if av:
            available.append((workers[worker], ch))
    available = sorted(available)
print(max(workers))
