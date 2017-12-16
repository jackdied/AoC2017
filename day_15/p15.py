import itertools as it
import re

'''
Generator A starts with 883
Generator B starts with 879
'''

starts = (883, 879)
factors = (16807, 48271)
divisor = 2147483647 # 2**31 - 1, I see what you did there

def genA(start):
    curr = start
    while True:
        curr = (curr * 16807) % divisor
        yield curr

def genB(start):
    curr = start
    while True:
        curr = (curr * 48271) % divisor
        yield curr

ita = genA(65)
assert (next(ita), next(ita), next(ita), next(ita)) == (1092455, 1181022009, 245556042,1744312007)
itb = genB(8921)
assert (next(itb), next(itb), next(itb), next(itb)) == (430625591, 1233683848, 1431495498, 137874439)


def match(a, b):
    a16 = a & 0xFFFF
    b16 = b & 0xFFFF
    return a16 == b16
assert not match(1092455, 430625591)
assert match(245556042, 1431495498)

def star1():
    #ita, itb = genA(65), genB(8921)
    ita, itb = genA(883), genB(879)
    good = 0
    for i in range(40_000_000):
        a, b = next(ita), next(itb)
        if match(a, b):
            good += 1
    print("GOOD", good)

star1()
'''
real    0m41.060s
user    0m39.598s
sys     0m0.310s
'''


def genA2(start):
    curr = start
    while True:
        curr = (curr * 16807) % divisor
        if curr % 4 == 0:
            yield curr

def genB2(start):
    curr = start
    while True:
        curr = (curr * 48271) % divisor
        if curr % 8 == 0:
            yield curr

ita = genA2(65)
assert (next(ita), next(ita), next(ita), next(ita)) == (1352636452, 1992081072, 530830436, 1980017072)
itb = genB2(8921)
assert (next(itb), next(itb), next(itb), next(itb)) == (1233683848, 862516352, 1159784568, 1616057672)

def star2():
    ita, itb = genA2(883), genB2(879)
    good = 0
    for i in range(5_000_000):
        a, b = next(ita), next(itb)
        if match(a, b):
            good += 1
    print("GOOD", good)

star2()
'''
real    0m19.311s
user    0m18.559s
sys     0m0.169s
'''
