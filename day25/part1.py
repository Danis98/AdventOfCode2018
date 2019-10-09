points = [list(map(lambda x: int(x), e.split(','))) for e in open('day25.input').read().strip().split()]

def manhattan(p1, p2):
    return sum([abs(p1[i]-p2[i]) for i in [0, 1, 2, 3]])

class disjoint_set:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def get_par(self, n):
        if n == self.par[n]:
            return n
        else:
            self.par[n] = self.get_par(self.par[n])
            return self.par[n]

    def join(self, a, b):
        pa = self.get_par(a)
        pb = self.get_par(b)
        if pa == pb:
            return
        self.par[pb] = pa

ds = disjoint_set(len(points))

for i in range(len(points)):
    for j in range(i+1, len(points)):
        if manhattan(points[i], points[j]) <= 3:
            ds.join(i, j)

roots = set()
for i in range(len(points)):
    roots.add(ds.get_par(i))

print(len(roots))
