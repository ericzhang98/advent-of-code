import collections
with open('input6.txt') as f:
    nums = list(map(int, f.readline().strip().split(',')))
cnts = collections.Counter(nums)
for _ in range(80):
    nxt = collections.Counter()
    for k, v in cnts.items():
        if k == 0:
            nxt[6] += v
            nxt[8] += v
        else:
            nxt[k-1] += v
    cnts = nxt
print(sum(nxt.values()))
