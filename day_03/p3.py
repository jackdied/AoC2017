import itertools as it


input = '312051'

def directions():
    yield 1, 0
    yield 0, -1
    yield -1, 0
    yield 0, 1

def move(point, direction):
    x, y = point
    dx, dy = direction
    return (x+dx, y+dy)

def yield_twice():
    curr = 1
    while True:
        yield curr
        yield curr
        curr += 1

def make_moves():
    pos = 0, 0
    nextdir_it = it.cycle(directions()) # loop forever on 4 direcctions
    move_counts = yield_twice()
    yield pos
    while True:
        for move_dir in it.repeat(next(nextdir_it),  next(move_counts)):
            pos = move(pos, move_dir)
            yield pos

input = 312051
tot_dx = tot_dy = 0

def calc_dist(n):
    tpos = (0, 0)
    for i, pos in enumerate(make_moves(), start=1):
        tpos = pos
        if i == n:
            break
    return abs(tpos[0]) + abs(tpos[1])

assert calc_dist(1) == 0
assert calc_dist(12) == 3, calc_dist(12)
assert calc_dist(23) == 2, calc_dist(23)
assert calc_dist(1024) == 31

# 559 is not the answer, try lower
    
print(calc_dist(input))


def neighs(pos):
    x, y = pos
    yield x-1, y
    yield x, y-1
    yield x+1, y
    yield x, y+1
    yield x-1, y-1
    yield x+1, y+1
    yield x+1, y-1
    yield x-1, y+1

assert 8 == len(list(set(neighs((0, 0)))))

from collections import defaultdict

def star2(at_least=1):
    cellvals = defaultdict(int)
    move_it = enumerate(make_moves(), start=1)
    i, pos = next(move_it)
    while True:
        if pos == (0, 0):  # first one is special
            score = 1
        else:
            score = sum(cellvals[p] for p in neighs(pos))
            #print("VALS", {k:v for (k,v) in cellvals.items() if v})
            #print("SUM", i, pos, [cellvals[p] for p in neighs(pos)], list(neighs(pos)))
        if score >= at_least:
            return i, score
        cellvals[pos] = score
        i, pos = next(move_it)


assert star2(1)[0] == 1, star2(1)
assert star2(2)[0] == 3, star2(2)
assert star2(3)[0] == 4, star2(3)
assert star2(4)[0] == 4, star2(3)
assert star2(5)[0] == 5, star2(3)

print(star2(input))
