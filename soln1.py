ans = 0
prv = float('inf')
with open('input1.txt') as f:
    for line in f.readlines():
        cur = int(line)
        if cur > prv:
            ans += 1
        prv = cur
print(ans)
