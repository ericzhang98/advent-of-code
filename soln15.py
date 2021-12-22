import heapq
lines = []
with open('a') as f:
    for line in f.readlines():
        lines.append(line.strip())
"""
g = []
for line in lines:
    g.append(list(map(int,list(line))))
m, n = len(g), len(g[0])
"""
m, n = len(lines), len(list(lines[0]))
g = [[0]*n*5 for _ in range(m*5)]
for i in range(m):
    for j in range(n):
        g[i][j] = int(lines[i][j])
        for di in range(5):
            for dj in range(5):
                i2,j2 = i+di*m,j+dj*n
                v = g[i][j]
                for _ in range(di+dj):
                    v += 1
                    if v == 10:
                        v = 1
                g[i2][j2] = v
                
        """
        g[i*5][j*5] = int(lines[i][j])
        for di in range(1,5):
            g[i*5+di][j*5] = (g[i*5+di-1][j*5] + 1)
            if g[i*5+di][j*5] == 10:
                g[i*5+di][j*5] = 1
        for di in range(5):
            for dj in range(1,5):
                g[i*5+di][j*5+dj] = (g[i*5+di][j*5+dj-1] + 1)
                if g[i*5+di][j*5+dj] == 10:
                    g[i*5+di][j*5+dj] = 1
        """
m, n = len(g), len(g[0])
print(m,n)
print(g)
    
dij = {(-1,0), (0,-1), (0,1), (1,0)}
def solve():
    seen = set()
    h = [(0, (0,0))]
    while h:
        d, pos = heapq.heappop(h)
        if pos in seen:
            continue
        seen.add(pos)
        i, j = pos
        if i == m-1 and j == n-1:
            return d
        for di, dj in dij:
            i2,j2 = i+di,j+dj
            if 0<=i2<m and 0<=j2<n:
                heapq.heappush(h, (d+g[i2][j2], (i2,j2)))
print(solve())
