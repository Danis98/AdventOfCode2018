from queue import Queue

regex = open("day20.input", "r").read().rstrip()

def parse_ast(s_idx, mode):
    elem = [mode]
    cur = ""
    idx = s_idx
    while idx < len(regex):
        if mode == 'AND':
            if regex[idx] in "NSWE":
                cur += regex[idx]
                idx += 1
            elif regex[idx] == '(':
                elem.append(cur)
                cur = ""
                n_elem, idx = parse_ast(idx+1, 'OR')
                elem.append(n_elem)
            elif regex[idx] in ')$':
                if regex[idx-1] != ')':
                    elem.append(cur)
                    cur = ""
                return elem, idx
            elif regex[idx] == '|':
                elem.append(cur)
                cur = ""
                return elem, idx
        if mode == 'OR':
            if regex[idx] == '|':
                if regex[idx+1] in '|)':
                    elem.append(['AND', ''])
                idx += 1
            elif regex[idx] == ')':
                return elem, idx+1
            else:
                n_elem, idx = parse_ast(idx, 'AND')
                elem.append(n_elem)

ast = parse_ast(1, 'AND')[0]

def print_ast(ast, depth=0):
    pref = '  '*depth
    print(pref + '[%s]'%ast[0])
    for elem in ast[1:]:
        if type(elem) is list:
            print_ast(elem, depth+1)
        else:
            print(pref + '  ' + elem)

#print_ast(ast)

def print_map():
    global base_map
    if len(base_map) == 0:
        return
    rs = [k[0] for k in base_map]
    cs = [k[1] for k in base_map]
    minr = min(rs)
    maxr = max(rs)
    minc = min(cs)
    maxc = max(cs)
    for r in range(minr, maxr+1):
        s = ""
        for c in range(minc, maxc+1):
            if (r, c) not in base_map:
                s += '#' if (r%2==1 and c%2==1) else ' '
            else:
                s += str(base_map[(r, c)])
        print(s)
    print("")

delta = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

base_map = {}

def generate_map(ast, cur_positions):
    global base_map
    for pos in cur_positions:
        base_map[pos] = '.'
        if (pos[0]-1, pos[1]) not in base_map:
            base_map[(pos[0]-1, pos[1])] = '#'
        if (pos[0]+1, pos[1]) not in base_map:
            base_map[(pos[0]+1, pos[1])] = '#'
        if (pos[0], pos[1]-1) not in base_map:
            base_map[(pos[0], pos[1]-1)] = '#'
        if (pos[0], pos[1]+1) not in base_map:
            base_map[(pos[0], pos[1]+1)] = '#'
    if ast[0] == 'AND':
        for seq in ast[1:]:
            if type(seq) is list:
                generate_map(seq, cur_positions)
            else:
                for k in range(len(cur_positions)):
                    pos = cur_positions[k]
                    for ch in seq:
                        pos = (pos[0]+delta[ch][0], pos[1]+delta[ch][1])
                        base_map[pos] = '~'
                        pos = (pos[0]+delta[ch][0], pos[1]+delta[ch][1])
                        base_map[pos] = '.'
                        if (pos[0]-1, pos[1]) not in base_map:
                            base_map[(pos[0]-1, pos[1])] = '#'
                        if (pos[0]+1, pos[1]) not in base_map:
                            base_map[(pos[0]+1, pos[1])] = '#'
                        if (pos[0], pos[1]-1) not in base_map:
                            base_map[(pos[0], pos[1]-1)] = '#'
                        if (pos[0], pos[1]+1) not in base_map:
                            base_map[(pos[0], pos[1]+1)] = '#'
                    cur_positions[k] = pos
    elif ast[0] == 'OR':
        npos = []
        for pos in cur_positions:
            for seq in ast[1:]:
                cur_pos = [pos]
                generate_map(seq, cur_pos)
                npos += cur_pos
        npos = list(set(npos))
        del cur_positions[:]
        for p in npos:
            cur_positions.append(p)

generate_map(ast, [(0, 0)])
#print_map()

dist = {}

for p in base_map:
    dist[p] = 1000000000 if base_map[p] != '#' else -1

dist[(0, 0)] = 0

def bfs():
    q = Queue()
    q.put((0, 0))
    while not q.empty():
        pos = q.get()
        if (pos[0]-1, pos[1]) in dist and dist[(pos[0]-1, pos[1])] > dist[pos] + 1:
            dist[(pos[0]-1, pos[1])] = dist[pos] + 1
            q.put((pos[0]-1, pos[1]))
        if (pos[0]+1, pos[1]) in dist and dist[(pos[0]+1, pos[1])] > dist[pos] + 1:
            dist[(pos[0]+1, pos[1])] = dist[pos] + 1
            q.put((pos[0]+1, pos[1]))
        if (pos[0], pos[1]-1) in dist and dist[(pos[0], pos[1]-1)] > dist[pos] + 1:
            dist[(pos[0], pos[1]-1)] = dist[pos] + 1
            q.put((pos[0], pos[1]-1))
        if (pos[0], pos[1]+1) in dist and dist[(pos[0], pos[1]+1)] > dist[pos] + 1:
            dist[(pos[0], pos[1]+1)] = dist[pos] + 1
            q.put((pos[0], pos[1]+1))

bfs()

maxd = 0
for p in dist:
    maxd = max(dist[p], maxd)

print(maxd/2)
