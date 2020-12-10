from queue import PriorityQueue

grid = open("day13.input", "r").read().rstrip().split("\n")

ROWS = len(grid)
COLS = max([len(line) for line in grid])

grid = [list(line.ljust(COLS)) for line in grid]

graph = [[] for i in range(ROWS*COLS)]

delta = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

left = {
    '>': '^',
    '<': 'v',
    '^': '<',
    'v': '>'
}

right = {
    '>': 'v',
    '<': '^',
    '^': '>',
    'v': '<'
}

carts = PriorityQueue()
cart_set = set()

for r in range(ROWS):
    for c in range(COLS):
        idx = COLS * r + c
        if grid[r][c] in '-><':
            graph[idx].append(idx+1)
            graph[idx].append(idx-1)
            if grid[r][c] in '<>':
                carts.put(((r, c), grid[r][c], 0))
                cart_set.add((r, c))
                grid[r][c] = '-'
        elif grid[r][c] in '|v^':
            graph[idx].append(idx+COLS)
            graph[idx].append(idx-COLS)
            if grid[r][c] in '^v':
                carts.put(((r, c), grid[r][c], 0))
                cart_set.add((r, c))
                grid[r][c] = '|'
        elif grid[r][c] == '+':
            graph[idx].append(idx+1)
            graph[idx].append(idx-1)
            graph[idx].append(idx+COLS)
            graph[idx].append(idx-COLS)
        elif grid[r][c] == '/' or grid[r][c] == '\\':
            if r > 0 and (grid[r-1][c] == '|' or grid[r-1][c] == '+'):
                graph[idx].append(idx-COLS)
            if r < ROWS-1 and (grid[r+1][c] == '|' or grid[r+1][c] == '+'):
                graph[idx].append(idx+COLS)
            if c > 0 and (grid[r][c-1] == '-' or grid[r][c-1] == '+'):
                graph[idx].append(idx-1)
            if c < COLS-1 and (grid[r][c+1] == '-' or grid[r][c+1] == '+'):
                graph[idx].append(idx+1)

collision = False
q2 = PriorityQueue()
while not collision:
    while not carts.empty():
        cart = carts.get()
        r, c = cart[0][0], cart[0][1]
        nr, nc = r+delta[cart[1]][0], c+delta[cart[1]][1]
        if (nr, nc) in cart_set:
            collision = True
            print("%d,%d" % (nc, nr))
            break
        cart_set.remove((r, c))
        cart_set.add((nr, nc))
        ndir = cart[1]
        nctr = cart[2]
        if grid[nr][nc] == '/':
            if cart[1] in '<>':
                ndir = left[cart[1]]
            elif cart[1] in '^v':
                ndir = right[cart[1]]
        elif grid[nr][nc] == '\\':
            if cart[1] in '<>':
                ndir = right[cart[1]]
            elif cart[1] in '^v':
                ndir = left[cart[1]]
        elif grid[nr][nc] == '+':
            if cart[2] == 0:
                ndir = left[cart[1]]
            elif cart[2] == 2:
                ndir = right[cart[1]]
            nctr = (cart[2] + 1) % 3
        q2.put(((nr, nc), ndir, nctr))
    carts, q2 = q2, carts
