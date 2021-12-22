ans = 0
x,y = 0,0
with open('input2.txt') as f:
    for line in f.readlines():
        action, amt = line.split()
        amt = int(amt)
        if action == 'forward':
            y += amt
        elif action == 'down':
            x += amt
        elif action == 'up':
            x -= amt
    print(x*y)
