lines = []
with open('input8.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
ans = 0
for line in lines:
    ten, four = line.split(" | ")
    for digit in four.split(" "):
        if len(digit) in {2, 3, 4, 7}:
            ans += 1
print(ans)
