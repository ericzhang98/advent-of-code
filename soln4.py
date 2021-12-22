lines = []
with open('input4.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
marks = list(map(int,lines[0].split(',')))
boards = []
board_states = []
for board_num in range((len(lines)-1) // 6):
    board = []
    for i in range(2+board_num*6, 2+board_num*6 + 5):
        line = lines[i]
        row = list(map(int,line.split()))
        board.append(row)
    boards.append(board)
    board_states.append([0]*10)
winner = None
last_mark = None
for mark in marks:
    for idx, board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == mark:
                    board_states[idx][i] += 1
                    board_states[idx][j+5] += 1
        if any(v == 5 for v in board_states[idx]):
            winner = idx
            last_mark = mark
            break
    if winner:
        break
seen_marks = set()
for mark in marks:
    seen_marks.add(mark)
    if mark == last_mark:
        break
ans = 0
for row in boards[winner]:
    for v in row:
        if v not in seen_marks:
            ans += v
ans *= last_mark
print(ans)
