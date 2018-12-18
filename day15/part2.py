from queue import Queue

orig_grid = [list(line) for line in open("day15.input", "r").read().rstrip().split("\n")]
grid = []

def print_grid():
    for r in range(len(grid)):
        s = ''.join(grid[r])+'  '
        for unit in sorted(units.keys()):
            if unit[0] == r:
                s += '%c(%d) ' % (grid[unit[0]][unit[1]], units[unit][1])
        print(s)

def is_in_range(pos):
    r, c = pos
    neigh = grid[r-1][c]+grid[r+1][c]+grid[r][c-1]+grid[r][c+1]
    return (grid[r][c] == 'E' and 'G' in neigh) or (grid[r][c] == 'G' and 'E' in neigh)

def get_dist(p1, p2):
    vis = {p1}
    q = Queue()
    q.put((0, p1))
    while not q.empty():
        cur_dist, cur_pos = q.get()
        r, c = cur_pos
        if cur_pos == p2:
            return cur_dist
        if (r-1, c) not in vis and grid[r-1][c] == '.' or (r-1, c) == p2:
            q.put((cur_dist+1, (r-1, c)))
            vis.add((r-1, c))
        if (r+1, c) not in vis and grid[r+1][c] == '.' or (r+1, c) == p2:
            q.put((cur_dist+1, (r+1, c)))
            vis.add((r+1, c))
        if (r, c-1) not in vis and grid[r][c-1] == '.' or (r, c-1) == p2:
            q.put((cur_dist+1, (r, c-1)))
            vis.add((r, c-1))
        if (r, c+1) not in vis and grid[r][c+1] == '.' or (r, c+1) == p2:
            q.put((cur_dist+1, (r, c+1)))
            vis.add((r, c+1))
    return -1

def find_enemies(pos):
    faction = grid[pos[0]][pos[1]]
    vis = {pos}
    q = Queue()
    q.put(pos)
    enemies = []
    while not q.empty():
        cur_pos = q.get()
        r, c = cur_pos
        if grid[r][c] != '.' and cur_pos != pos:
            if (faction == 'E' and grid[r][c] == 'G') or (faction == 'G' and grid[r][c] == 'E'):
                enemies.append(cur_pos)
            continue
        if (r-1, c) not in vis:
            q.put((r-1, c))
            vis.add((r-1, c))
        if (r+1, c) not in vis:
            q.put((r+1, c))
            vis.add((r+1, c))
        if (r, c-1) not in vis:
            q.put((r, c-1))
            vis.add((r, c-1))
        if (r, c+1) not in vis:
            q.put((r, c+1))
            vis.add((r, c+1))
    return enemies

def move(pos):
    enemies = find_enemies(pos)
    in_range = []
    for enemy in enemies:
        r, c = enemy
        if grid[r-1][c] == '.':
            d = get_dist(pos, (r-1, c))
            if d != -1:
                in_range.append((d, (r-1, c)))
        if grid[r+1][c] == '.':
            d = get_dist(pos, (r+1, c))
            if d != -1:
                in_range.append((d, (r+1, c)))
        if grid[r][c-1] == '.':
            d = get_dist(pos, (r, c-1))
            if d != -1:
                in_range.append((d, (r, c-1)))
        if grid[r][c+1] == '.':
            d = get_dist(pos, (r, c+1))
            if d != -1:
                in_range.append((d, (r, c+1)))
    if len(in_range) == 0:
        return pos
    target = sorted(in_range)[0]
    moves = []
    r, c = pos
    if grid[r-1][c] == '.':
        d = get_dist(target[1], (r-1, c))
        if d != -1:
            moves.append((d, (r-1, c)))
    if grid[r+1][c] == '.':
        d = get_dist(target[1], (r+1, c))
        if d != -1:
            moves.append((d, (r+1, c)))
    if grid[r][c-1] == '.':
        d = get_dist(target[1], (r, c-1))
        if d != -1:
            moves.append((d, (r, c-1)))
    if grid[r][c+1] == '.':
        d = get_dist(target[1], (r, c+1))
        if d != -1:
            moves.append((d, (r, c+1)))
    return sorted(moves)[0][1]


def attack(pos):
    global elves, goblins
    enemy_pos = find_enemies(pos)
    enemies = [(get_dist(en_pos, pos), units[en_pos][1], en_pos) for en_pos in enemy_pos]
    target = sorted(enemies)[0][2]
    units[target] = (units[target][0], units[target][1] - units[pos][0])
    if units[target][1] <= 0:
        units.pop(target)
        if grid[target[0]][target[1]] == 'G':
            goblins -= 1
        elif grid[target[0]][target[1]] == 'E':
            elves -= 1
        grid[target[0]][target[1]] = '.'

units = {}
elves = goblins = 0
turn = 0

def init_grid(atk):
    global elves, goblins, turn, grid, units
    elves = goblins = 0
    turn = 1
    grid = [line[:] for line in orig_grid]
    units = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] not in 'GE':
                continue
            if grid[r][c] == 'G':
                goblins += 1
                units[(r, c)] = (3, 200)
            elif grid[r][c] == 'E':
                elves += 1
                units[(r, c)] = (atk, 200)

def solve_grid():
    global goblins, elves, turn
    orig_goblins = goblins
    orig_elves = elves
    while True:
        unit_pos = sorted(list(units.keys()))
        for unit in unit_pos:
            if unit not in units:
                continue
            if goblins == 0:
                turn -= 1
                break
            atk = units[unit][0]
            hp = units[unit][1]
            pos = unit
            if not is_in_range(unit):
                next_pos = move(unit)
                if next_pos != unit:
                    units.pop(unit)
                    units[next_pos] = (atk, hp)
                    grid[next_pos[0]][next_pos[1]] = grid[unit[0]][unit[1]]
                    grid[unit[0]][unit[1]] = '.'
                pos = next_pos
            if is_in_range(pos):
                attack(pos)

        #print_grid()
        if orig_elves > elves:
            return -1
        if goblins == 0:
            break
        turn += 1

    hp_sum = sum([units[unit][1] for unit in units])
    
    return turn*hp_sum

atk_a = 4
atk_b = 200
while atk_a < atk_b:
    atk = int((atk_a+atk_b)/2)
    init_grid(atk)
    res = solve_grid()
    if res == -1:
        atk_a = atk + 1
    else:
        atk_b = atk
    #print(atk, "=>", res)
    #print(atk_a, atk_b)

init_grid(atk_b)
print(solve_grid())
