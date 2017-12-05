import itertools as it

my_input = [int(x.strip()) for x in open('input.txt').readlines()]
print(my_input)

def star1():
    regs = dict(enumerate(my_input))
    curr = 0
    steps = 0
    while True:
        try:
            jump = regs[curr]
        except LookupError:
            print(steps)
            return
        regs[curr] += 1
        curr = curr+jump
        steps += 1
    return

def star2():
    regs = dict(enumerate(my_input))
    curr = 0
    steps = 0
    while True:
        try:
            jump = regs[curr]
        except LookupError:
            print(steps)
            return
        if jump >= 3:
            regs[curr] -= 1
        else:
            regs[curr] += 1
        curr += jump
        steps += 1
    return


if __name__ == '__main__':
    star1()
    # not 52531
    # not 1074
    # not 364540
    star2()
