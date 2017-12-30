
import itertools as it
from collections import deque

inp = list(map(int, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'.split(',')))
ord_inp = list(map(ord, '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'))

def transform(lens=[], start_nums=list(range(256)), repeat=1):
    curr = 0
    skip = 0
    nums = deque(start_nums)
    total_rotates = 0
    orig_lens = lens
    for _ in range(repeat):
        lens = list(orig_lens)
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


#
# Star2
#

extra_seeds = [17, 31, 73, 47, 23]
star2_inp = ord_inp + extra_seeds

def dense_hash(sparse_hash):
    sparse_hash = list(sparse_hash)
    result = []
    while sparse_hash:
        sixteen = sparse_hash[:16]
        sparse_hash[:16] = []
        cum = 0
        for num in sixteen:
            cum ^= num
        result.append(cum)
    return result

# from the problem desc
sparse = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
assert dense_hash(sparse) == [64]
assert dense_hash(sparse+sparse) == [64, 64], dense_hash(sparse+sparse)

def hexify(nums):
    def pad_hex(i):
        """ hex(7) => '0x7' but we want '07' """
        pure_hex = hex(i)
        short_hex = pure_hex[len('0x'):]
        return ('00'+short_hex)[-2:]
    return ''.join(pad_hex(n) for n in nums)

assert hexify([64, 7, 255]) == '4007ff', hexify([64, 7, 255])

def total_transform(lens):
    result = transform(lens+extra_seeds, repeat=64)
    dense = dense_hash(result)
    return hexify(dense)

assert 'a2582a3a0e66e6e86e3812dcb672a272' == total_transform([]), total_transform([])
assert '33efeb34ea91902bb2f59c9920caa6cd' == total_transform(list(map(ord, 'AoC 2017')))

print("STAR2", total_transform(ord_inp))
