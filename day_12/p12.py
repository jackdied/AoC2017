import itertools as it
import re


def pairs(filename='input.txt'):
    for line in open(filename).readlines():
        m = re.match('(\d+) <-> (.*)', line)
        start, rest = m.groups()
        left = int(start)
        rest = [int(x.strip()) for x in rest.split(',')]
        yield left, rest

def star1(edges, start=0):
    d = dict(edges)
    dist = {}  # {end: dist_from_start}
    stack = [(start, 0)]  # (curr, dist)
    while stack:
        curr, n = stack.pop(0)
        for other in d.get(curr, []):
            if other in dist:
                continue
            stack.append((other, n+1))
            dist[other] = n+1
    print("REACHABLE", len(dist))

def star2(edges):
    d = dict(edges)
    groups = []
    while d:
        dist = {}  # {end: dist_from_start}
        groups.append(dist)
        start = next(iter(d))
        stack = [(start, 0)]  # (curr, dist)
        dist[start] = 0
        while stack:
            curr, n = stack.pop(0)
            for other in d.pop(curr, []):
                if other in dist:
                    continue
                stack.append((other, n+1))
                dist[other] = n+1

    print("GROUPS", len(groups), [len(g) for g in groups])


star1(pairs())
star2(pairs())
