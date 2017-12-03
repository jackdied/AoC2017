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

def make_spiral(n, start=(0,0)):
    pos = start
    curr = 0
    nextdir_it = it.cycle(directions()) # loop forever on 4 direcctions
    move_counts = yield_twice()
    yield pos, curr
    curr += 1
    while curr < n:
        move_dir = next(nextdir_it)
        move_count = next(move_counts)
        for _ in range(move_count):
            #print("MOVE", move_count, move_dir, pos)
            pos = move(pos, move_dir)
            yield pos, curr
            curr += 1

def make_grid(n):
    width = height = n
    grid = [[0 for x in range(width)] for y in range(height)]
    pairs = list(make_spiral(n, (width//2, height//2)))
    #print("PAIRS", pairs)
    for (x,y),v in pairs:
        grid[y][x] = v
    return grid

def make_moves(n):
    pos = 0, 0
    curr = 1
    nextdir_it = it.cycle(directions()) # loop forever on 4 direcctions
    move_counts = yield_twice()
    yield pos, curr
    curr += 1
    while curr < n:
        move_dir = next(nextdir_it)
        move_count = next(move_counts)
        for _ in range(move_count):
            pos = move(pos, move_dir)
            yield pos, curr
            if curr == n:
                break
            curr += 1


input = 312051
tot_dx = tot_dy = 0

def calc_dist(n):
    tpos = [0, 0]
    for pos, v in make_moves(n):
        tpos = pos
    return abs(tpos[0]) + abs(tpos[1])

assert calc_dist(1) == 0
assert calc_dist(12) == 3, calc_dist(12)
assert calc_dist(23) == 2, calc_dist(23)
assert calc_dist(1024) == 31

# 559 is not the answer, try lower
    
print(calc_dist(input))
