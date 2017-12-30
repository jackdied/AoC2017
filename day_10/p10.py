
import itertools as it
from collections import deque

inp = list(map(int, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'.split(',')))
ord_inp = list(map(ord, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'))

def star1(nums, lens):
    nums = deque(nums)
    curr = 0
    skip = 0
    for l in lens:
        new_nums = list(nums)
        new_nums[:l] = new_nums[:l][::-1]
        nums = deque(new_nums)
        move = l + skip
        skip += 1
        nums.rotate(-move)
        curr = (curr + move) % len(nums)
    nums.rotate(curr)
    #return curr % len(nums), skip, nums
    return nums[0] * nums[1]

print(star1(range(5), [3, 4, 1, 5]))

print(star1(range(256), inp)) # 52070


def star2(txt, nums=list(range(256)), cycles=64):
    nums = deque(nums)
    lens = nums + [17, 31, 73, 47, 23]
    curr = 0
    skip = 0
    for _ in range(cycles):
        for l in lens:
            new_nums = list(nums)
            new_nums[:l] = new_nums[:l][::-1]
            nums = deque(new_nums)
            move = l + skip
            skip += 1
            nums.rotate(-move)
            curr = (curr + move) % len(nums)
        nums.rotate(curr)
    return list(nums)


def hashify(nums):
    out = []
    while nums:
        sixteen = nums[:16]
        nums[:16] = []
        xored = sixteen[0]
        for n in sixteen[1:]:
            xored ^= n
        out.append(xored)
    return ''.join(hex(n)[-2:] for n in out)

print("DONE", hashify(star2(range(256), ord_inp)))
        
        
