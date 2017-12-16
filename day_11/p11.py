import itertools as it


move_delta = {'n': (0, -2),
              'ne': (1, -1),
              'se': (1, 1),
              's': (0, 2),
              'sw': (-1, 1),
              'nw': (-1, -1),
             }

def move(pos, dir):
    x, y = pos
    dx, dy = move_delta[dir]
    return (x+dx, y+dy)

inps = open('input.txt').read().strip().split(',')

def dist(a, b):
    vert = abs(a[1] - b[1])
    horiz = abs(a[0] - b[0])
    moves = 0
    while vert >= horiz+2:
        vert -= 2
        moves += 1
    moves += horiz
    return moves

def here_to_there(start, end):
    curr = start
    moves = []
    while curr != end:
        best = sorted((move(curr, d) for d in move_delta), key=lambda x:dist(end, x))[0]
        moves.append(best)
        curr = best
    print("LEN MOVES", len(moves))
    print("BESTDIST", dist(start, end))

def star1(moves=[]):
    pos = (0, 0)
    for mv in moves:
        pos = move(pos, mv)
    print("END", pos)
    here_to_there(pos, (0,0))


#star1('ne,ne,ne'.split(','))
#star1('ne,ne,sw,sw'.split(','))
#star1('ne,ne,s,s'.split(','))
#star1('se,sw,se,sw,sw'.split(','))

def star2(moves):
    start = pos = (0, 0)
    farthest = 0
    for mv in moves:
        pos = move(pos, mv)
        farthest = max(farthest, dist(start, pos))
    print("FAR", farthest)



star1(inps)
star2(inps)
