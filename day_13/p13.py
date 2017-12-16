import itertools as it
import re

def read_input():
    for line in open('input.txt').readlines():
        line = line.strip()
        depth, rng = [int(x) for x in line.split(': ')]
        yield depth, rng

def star1(pairs):
    pairs = list(pairs)
    costs = {a:a*b for (a,b) in pairs}
    rows = {}
    for i, rng in pairs:
        nums = list(range(rng))
        all_nums = nums + nums[1:-1][::-1]
        print((i, all_nums))
        rows[i] = it.cycle(all_nums)
    curr = 0
    caught = []
    while curr <= max(iter(rows)):
        where = {i:next(x) for (i, x) in rows.items()}
        if where.get(curr, -1) == 0:
            caught.append(curr)
        curr += 1
    print("CAUGHT", caught, sum(costs[n] for n in caught))

def star2(pairs):
    pairs = list(pairs)
    bad_every = {}
    for i, rng in pairs:
        nums = list(range(rng))
        all_nums = nums + nums[1:-1][::-1]
        bad_every[i] = len(all_nums)
        #print("BAD", i, len(nums), all_nums)

    delay = 0
    curr = 0
    best = 0
    while curr <= 96:
        curr = 0
        while curr <= 96:
            every = bad_every.get(curr, -1)
            if every == -1:
                is_bad = False
            else:
                is_bad = ((delay+curr) % every) == 0
            if is_bad:
                delay += 1
                break
            curr += 1
            best = max(best, curr)
        print("DELAY", delay, curr, best)
       

inp = list(read_input())
#inp = [(0,3), (1,2), (4,4), (6,4)]

star1(inp)
star2(inp)

'''
time star2(inp)
real    0m45.549s
user    0m29.009s
sys     0m6.715s
'''
