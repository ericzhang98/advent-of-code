lines = []
with open('input22.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())
steps = []
for line in lines:
    on, rest = line.split(" ")
    x, y, z = rest.split(",")
    x1, x2 = x.split("=")[1].split("..")
    y1, y2 = y.split("=")[1].split("..")
    z1, z2 = z.split("=")[1].split("..")
    steps.append((on == 'on', int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)))
#print(steps)
"""
cube = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]
def clip(a,b):
    if a > 50:
        return 51, 51
    if b < -50:
        return -51, -51
    if a <= -50:
        a = -50
    if b >= 50:
        b = 50
    return a,b
for on, x1, x2, y1, y2, z1, z2 in steps:
    x1, x2 = clip(x1,x2)
    y1, y2 = clip(y1,y2)
    z1, z2 = clip(z1,z2)
    for xi in range(x1,x2+1):
        for yi in range(y1,y2+1):
            for zi in range(z1,z2+1):
                if 0<=xi+50<101 and 0<=yi+50<101 and 0<=zi+50<101:
                    #print(xi+50,yi+50,zi+50)
                    #print(xi,yi,zi)
                    cube[xi+50][yi+50][zi+50] = on
    #print(sum(sum(sum(v) for v in a) for a in cube))

print(sum(sum(sum(v) for v in a) for a in cube))
"""

# for each on cube:
#   calculate vol(intersection with all cuboids after), which is equivalent to vol(union of all clipped cuboids after)
#   ans += vol(cube) - vol(intersection)

# get all disjoint rectangles and how much each cube contributes to each rectangle
# volume = sum of (disjoint rectangle area) * (merge interval length of each cubes contribution)
def cuboid_union_volume(cubes):
    if len(cubes) == 0:
        return 0
    x_points = set()
    y_points = set()
    for x1, x2, y1, y2, z1, z2 in cubes:
        x_points |= {x1, x2}
        y_points |= {y1, y2}
    x_points = sorted(list(x_points))
    y_points = sorted(list(y_points))
    import collections
    segments = collections.defaultdict(list)
    for i in range(len(x_points)-1):
        for j in range(len(y_points)-1):
            rect_x1, rect_x2, rect_y1, rect_y2 = x_points[i], x_points[i+1], y_points[j], y_points[j+1]
            for x1, x2, y1, y2, z1, z2 in cubes:
                if x1 <= rect_x1 <= rect_x2 <= x2 and y1 <= rect_y1 <= rect_y2 <= y2:
                    segments[(rect_x1, rect_x2, rect_y1, rect_y2)].append((z1,z2))
    volume = 0
    for k, v in segments.items():
        x1, x2, y1, y2 = k
        area = (x2-x1) * (y2-y1)
        length = merge_interval_length(v)
        volume += area * length
    return volume

def merge_interval_length(intervals):
    l = []
    for s, e in intervals:
        l.append((s,float('-inf'), 1))
        l.append((e,float('inf'), -1))
    l.sort()
    merged = []
    cnt = 0
    curr_start = 0
    for t, _, dcnt in l:
        if dcnt == 1:
            if cnt == 0:
                curr_start = t
            cnt += 1
        else:
            cnt -= 1
            if cnt == 0:
                merged.append((curr_start, t))
    return sum(interval[1] - interval[0] for interval in merged)

def clip_cube(cube, anticube):
    x1 = max(cube[0], anticube[0])
    x2 = min(cube[1], anticube[1])
    y1 = max(cube[2], anticube[2])
    y2 = min(cube[3], anticube[3])
    z1 = max(cube[4], anticube[4])
    z2 = min(cube[5], anticube[5])
    #print('clip cube', cube, anticube, (x1,x2,y1,y2,z1,z2))
    if x2 < x1 or y2 < y1 or z2 < z1:
        return None
    return (x1,x2,y1,y2,z1,z2)

#print(steps)
ans = 0
for i in range(len(steps)):
    on, x1, x2, y1, y2, z1, z2 = steps[i]
    main_cube = (x1,x2,y1,y2,z1,z2)
    if not on:
        continue
    og_vol = (x2+1-x1) * (y2+1-y1) * (z2+1-z1)
    anti_cubes = []
    for j in range(i+1, len(steps)):
        anti_cube = steps[j][1:]
        anti_cube = clip_cube(main_cube, anti_cube)
        if anti_cube is not None:
            anti_cubes.append(anti_cube)
    #print(x1,x2,y1,y2,z1,z2)
    #print(anti_cubes)
    anti_vol = cuboid_union_volume(anti_cubes)
    #print(og_vol, anti_vol, og_vol - anti_vol)
    ans += og_vol - anti_vol

print(ans)
