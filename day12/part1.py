lines = open("day12.input", "r").read().rstrip().split("\n")

def get_neighbors(idx):
    s = ''
    for i in range(idx-2, idx+3):
        if i in state and state[i] == '#':
            s += '#'
        else:
            s += '.'
    return s

init_state = lines[0].split(":")[1][1:]

minP = 0
maxP = len(init_state)-1

rules = {}
for line in lines[2:]:
    r, n = line.split(" => ")
    rules[r] = n

state = {}
nxt = {}
for i in range(len(init_state)):
    state[i] = init_state[i]

#print(init_state)
for gen in range(20):
    g = ""
    for p in range(minP-2, maxP+3):
        n = rules[get_neighbors(p)] if get_neighbors(p) in rules else '.'
        if n == '#':
            minP = min(p, minP)
            maxP = max(p, maxP)
        nxt[p] = n
        g += n
    state = dict(nxt)
    nxt.clear()
    #print(g)

tot = 0
for n in state:
    if state[n] == '#':
        tot += n
print(tot)
