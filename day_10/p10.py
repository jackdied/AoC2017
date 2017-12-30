
import itertools as it
from collections import deque

inp = list(map(int, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'.split(',')))
ord_inp = list(map(ord, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'))

def transform(lens=[], start_nums=list(range(256))):
    curr = 0
    skip = 0
    nums = deque(start_nums)
    total_rotates = 0
    for clen in lens:
        lnums = list(nums)
        # reverse clen items, starting at curr
        cp = list(nums)
        cp[curr:clen] = cp[curr:clen][::-1]
        nums = deque(cp)
        # move the curr position forward by clen + skip
        do_rotate = clen + skip
        total_rotates += do_rotate
        nums.rotate(-do_rotate)
        # increment skip
        skip += 1
    # rotate like we were keeping track of curr
    nums.rotate(-(len(nums) - total_rotates % len(nums)))
    return list(nums)

# from the problem description
assert transform([3, 4, 1, 5], [0, 1, 2, 3, 4]) == [3, 4, 2, 1, 0]

def score(nums):
    return nums[0] * nums[1]

# my original correct answer to star1, given my input
assert 52070 == score(transform(inp))

