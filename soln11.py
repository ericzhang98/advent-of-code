import collections
lines = []
with open('ex11.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
g = []
for line in lines:
    g.append(list(map(int,list(line))))
m, n = len(g), len(g[0])
dij = {(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)}
def step(g):
    flashes = set()
    nxt = [[None]*n for _ in range(m)]
    q = collections.deque()
    for i in range(m):
        for j in range(n):
            if g[i][j] == 9:
                q.append((i,j))
    while q:
        i, j = q.popleft()
        for di, dj in dij:
            i2, j2 = i+di, j+dj

    return nxt, len(flashes)
ans = 0
for _ in range(100):
    g, flashes = step(g)
    ans += flashes
print(ans)
