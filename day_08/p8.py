import itertools as it
import re

def star1():
    myloc = {}
    best = 0
    for line in open('input.txt').readlines():
        line = line.strip()
        reg_d, cmd, val, iff, reg_s, cmp, cmp_val  = line.split()
        myloc.setdefault(reg_d, 0)
        myloc.setdefault(reg_s, 0)
        doit = reg_s + ' ' + cmp + ' ' + cmp_val
        test = eval(doit, {}, myloc)
        if test:
            if cmd == 'inc':
                myloc[reg_d] += int(val)
            elif cmd == 'dec':
                myloc[reg_d] -= int(val)
            else:
                raise ValueError(cmd)
        best = max(best, max(myloc.values()))
        print("MAX", best)
def star2():
    return


star1()
star2()
