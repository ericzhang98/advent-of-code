with open('input17.txt') as f:
    line = f.readline().strip()
print(line.split(" "))
x, y = line.split(" ")[2:4]
x1, x2 = map(int,x.split("=")[1][:-1].split(".."))
y1, y2 = map(int,y.split("=")[1].split(".."))
print(x1,x2,y1,y2)

def simulate(vx,vy):
    print('sim',vx,vy)
    cx, cy = 0, 0
    while True:
        print(cx,cy)
        if cx > x2:
            return False
        if cy < y1:
            return False
        if x1<=cx<=x2 and y1<=cy<=y2:
            return True
        cx += vx
        cy += vy
        vx = max(0, vx-1)
        vy -= 1

ans = 0
total_cnt = 0
for vx in range(x2+1):
    for vy in range(y1,abs(y1)+1):
        if simulate(vx,vy):
            total_cnt += 1
            print('works',vx,vy)
            ans = max(ans, vy)

print(ans*(ans+1)//2)
print(total_cnt)

# there was no elegant solution rip
"""
y1,y2 = abs(y1),abs(y2)
# valid_y = list(range(y1,y2+1))
def y_range(vy):
    pass

for vy in range(y1):
    cur = 0
    while True:
        cur += vy


def x_range():
    if x1 == 0:
        return [0 , float('inf')]

    def vx_range(vx):
        pass

    for vx in range(0, x2):
        vx_range(vx)


    cnt = 0
    cur = 0
    if x1 <= 0 <= x2:
        mi = 0
    else:
        while cur < x1:
            if vx == 0:
                return None
            cur += vx
            vx -= 1
            cnt += 1
        mi = cnt
    while cur <= x2:
        if vx == 0:
            cnt = float('inf')
            break
        cur += vx
        vx -= 1
        cnt += 1
"""
