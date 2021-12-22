"""
p1, p2 = 4, 2
s1, s2 = 0, 0
die = 1
roll_cnt = 0
turn_one = True
while True:
    if s1 >= 1000 or s2 >= 1000:
        break
    if turn_one:
        for _ in range(3):
            p1 += die
            die += 1
            if die > 100:
                die -= 100
            roll_cnt += 1
        while p1 > 10:
            p1 -= 10
        s1 += p1
    else:
        for _ in range(3):
            p2 += die
            die += 1
            if die > 100:
                die -= 100
            roll_cnt += 1
        while p2 > 10:
            p2 -= 10
        s2 += p2
    turn_one = not turn_one
print(s1, s2, roll_cnt)
print(min(s1, s2) * roll_cnt)
"""

import collections
import itertools
# (p1, p2, s1, s2, p1_turn, p1_won) -> cnt
pstate = {(4,2,0,0,True,None): 1}
die_counts = collections.Counter(sum(combo) for combo in itertools.product([1,2,3], repeat=3))
print(die_counts)
while any(k[5] is None for k in pstate):
    pstate_nxt = collections.Counter()
    for state_k, state_cnt in pstate.items():
        if state_k[5] is not None:
            pstate_nxt[(state_k)] += state_cnt
            continue
        if state_k[5] is None:
            for die_k, die_count in die_counts.items():
                p1, p2, s1, s2, p1_turn, p1_won = state_k
                if p1_turn:
                    p1 += die_k
                    while p1 > 10:
                        p1 -= 10
                    s1 += p1
                    if s1 >= 21:
                        p1_won = True
                else:
                    p2 += die_k
                    while p2 > 10:
                        p2 -= 10
                    s2 += p2
                    if s2 >= 21:
                        p1_won = False
                p1_turn = not p1_turn
                pstate_nxt[(p1, p2, s1, s2, p1_turn, p1_won)] += state_cnt * die_count
    pstate = pstate_nxt
print(sum(v for k,v in pstate.items() if k[5] == True))
print(sum(v for k,v in pstate.items() if k[5] == False))
