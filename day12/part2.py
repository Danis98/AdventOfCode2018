lines = open("day12.input", "r").read().rstrip().split("\n")

def get_neighbors(idx):
    s = ''
    for i in range(idx-2, idx+3):
        if i in state and state[i] == '#':
            s += '#'
        else:
            s += '.'
    return s

def is_shifted(s1, s2):
    sr = True
    sl = True
    for n in s2:
        if (n-1 in s1 and s1[n-1] != s2[n]) or (n-1 not in s1 and s2[n] == '#'):
            sr = False
            break
    for n in s2:
        if (n+1 in s1 and s1[n+1] != s2[n]) or (n+1 not in s1 and s2[n] == '#'):
            sl = False
            break
    return 1 if sr else -1 if sl else 0

def get_val(s):
    tot = 0
    for n in s:
        if s[n] == '#':
            tot += n
    return tot

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

MAX_ITER = 50000000000
for gen in range(1, MAX_ITER+1):
    g = ""
    for p in range(minP-2, maxP+3):
        n = rules[get_neighbors(p)] if get_neighbors(p) in rules else '.'
        if n == '#':
            minP = min(p, minP)
            maxP = max(p, maxP)
        nxt[p] = n
        g += n
    sh = is_shifted(state, nxt)
    #print(g)
    if(state == nxt):
        print(get_val(state))
        break
    if sh != 0:
        cnt = 0
        for n in state:
            if state[n] == '#':
                cnt += 1
        print(get_val(nxt) + sh*cnt*(MAX_ITER-gen))
        break
    state = dict(nxt)
    nxt.clear()
