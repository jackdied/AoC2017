import itertools as it

my_input = '''14    0    15    12    11    11    3    5    1    6    8    4    9    1    8    4'''
for i in range(10):
    my_input = my_input.replace('  ', ' ')
print("INP", my_input)
my_input = list(map(int, my_input.split(' ')))

#my_input = [0, 2, 7, 0]

def star1():
    seen = set()
    curr = my_input
    steps = 0
    while tuple(curr) not in seen:
        seen.add(tuple(curr))
        max_s = max(curr)
        i = 0
        for i, size in enumerate(curr):
            if size == max_s:
                break
        curr[i] = 0
        n = i
        while max_s:
            max_s -= 1
            n = (n+1) % len(curr)
            curr[n] += 1
        steps += 1
    print("STEPS", steps)
    return

def star2():
    seen = set()
    seen2 = set()
    curr = my_input
    steps = 0
    while tuple(curr) not in seen:
        seen.add(tuple(curr))
        max_s = max(curr)
        i = 0
        for i, size in enumerate(curr):
            if size == max_s:
                break
        curr[i] = 0
        n = i
        while max_s:
            max_s -= 1
            n = (n+1) % len(curr)
            curr[n] += 1
        steps += 1

    steps = 0
    while tuple(curr) not in seen2:
        seen2.add(tuple(curr))
        max_s = max(curr)
        i = 0
        for i, size in enumerate(curr):
            if size == max_s:
                break
        curr[i] = 0
        n = i
        while max_s:
            max_s -= 1
            n = (n+1) % len(curr)
            curr[n] += 1
        steps += 1
    print("STEPS", steps)
    return

if __name__ == '__main__':
    star1()
    star2()
