lines = []
with open('input3.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
arr = [0] * len(lines[0])
for line in lines:
    for i, v in enumerate(map(int, list(line))):
        if v == 0:
            arr[i] -= 1
        else:
            arr[i] += 1
gamma = "".join(map(str, (map(lambda v: 0 if v < 0 else 1, arr))))
gamma = int(gamma, 2)
epsilon = "".join(map(str, (map(lambda v: 0 if v > 0 else 1, arr))))
epsilon = int(epsilon, 2)

print(int(gamma) * int(epsilon))
