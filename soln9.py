with open('input9.txt') as f:
    lines = [line.strip() for line in f.readlines()]
g = [list(map(int,list(line))) for line in lines]
m, n = len(g), len(g[0])
dij = [(0,1),(0,-1),(1,0),(-1,0)]
ans = 0
for i in range(m):
    for j in range(n):
        neigh = [(i+di,j+dj) for di,dj in dij if 0<=i+di<m and 0<=j+dj<n]
        if all(g[i2][j2] > g[i][j] for i2,j2 in neigh):
            ans += g[i][j] + 1
print(ans)
