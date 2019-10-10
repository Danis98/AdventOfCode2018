grid = [list(line) for line in open("day18.input", "r").read().rstrip().split("\n")]

MAX_TURNS = 10

turn = 1

def get_neigh(r, c):
    ctr = {'.':0, '|':0, '#':0}
    for rr in range(max(0, r-1), min(r+2, len(grid))):
        for cc in range(max(0, c-1), min(c+2, len(grid[rr]))):
            if (rr, cc) == (r, c):
                continue
            ctr[grid[rr][cc]] += 1
    return ctr

while turn <= MAX_TURNS:
    n_grid = [['' for i in range(len(grid[j]))] for j in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            neigh = get_neigh(r, c)
            if grid[r][c] == '.' and neigh['|'] >= 3:
                n_grid[r][c] = '|'
            elif grid[r][c] == '|' and neigh['#'] >= 3:
                n_grid[r][c] = '#'
            elif grid[r][c] == '#' and not (neigh['#'] >= 1 and neigh['|'] >= 1):
                n_grid[r][c] = '.'
            else:
                n_grid[r][c] = grid[r][c]
    grid = n_grid

    turn += 1

trees = lumber = 0
for line in grid:
    for e in line:
        if e == '|':
            trees += 1
        elif e == '#':
            lumber += 1

print(trees*lumber)
