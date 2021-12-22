import collections
lines = []
with open('input5.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
for i in range(len(lines)):
    p1, p2 = lines[i].split(" -> ")
    x1,y1 = map(int,p1.split(','))
    x2,y2 = map(int,p2.split(','))
    if x2 < x1:
        x1,x2 = x2,x1
    if y2 < y1:
        y1,y2 = y2,y1
    lines[i] = (x1,y1,x2,y2)
cnts = collections.Counter()
for x1,y1,x2,y2 in lines:
    if x1==x2:
        for y in range(y1,y2+1):
            cnts[(x1,y)] += 1
    elif y1==y2:
        for x in range(x1,x2+1):
            cnts[(x,y1)] += 1
print(sum(v >= 2 for v in cnts.values()))
