lines = []
with open('ex10.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
ans = 0
closing = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
}
points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
}
def score(line):
    stack = []
    for c in list(line):
        if c in {'(', '[', '{', '<'}:
            stack.append(c)
        else:
            if stack[-1] == closing[c]:
                stack.pop()
            else:
                return points[c]
    return 0
for line in lines:
    ans += score(line)
print(ans)
